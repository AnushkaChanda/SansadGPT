from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from ddgs import DDGS


# ================== LOAD EMBEDDINGS ==================
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ================== LOAD FAISS ==================
vectorstore = FAISS.load_local(
    "sansad_faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 6})


# ================== LOAD LLM ==================
pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=700,
    temperature=0.3
)

llm = HuggingFacePipeline(pipeline=pipe)


# ================== UTIL FUNCTIONS ==================
def is_time_sensitive(query: str) -> bool:
    keywords = [
        "today", "current", "latest", "now",
        "fuel", "price", "gdp", "inflation",
        "rate", "recent"
    ]
    return any(k in query.lower() for k in keywords)


def web_search(query: str):
    with DDGS() as ddgs:
        return list(ddgs.text(query, max_results=5))


def clean_docs(docs):
    """Remove useless header-only chunks"""
    cleaned = []
    for d in docs:
        text = d.page_content.strip()
        if len(text) < 200:
            continue
        if "Written Answers to" in text and len(text) < 500:
            continue
        cleaned.append(text)
    return cleaned


# ================== MAIN FUNCTION ==================
def sansad_gpt(query: str):
    """
    Returns:
    {
        "answer": str,
        "source": "Web (Internet Search)" | "Parliamentary Records"
    }
    """

    # 🌐 ========== WEB MODE ==========
    if is_time_sensitive(query):
        results = web_search(query)

        if not results:
            return {
                "answer": "No recent information was found on the internet.",
                "source": "Web (Internet Search)"
            }

        context = ""
        for r in results[:3]:
            context += f"{r.get('title', '')}: {r.get('body', '')}\n"

        prompt = f"""
Answer the question clearly and factually using the information below.

Information:
{context}

Question:
{query}
"""

        answer = llm.invoke(prompt)

        return {
            "answer": answer.strip(),
            "source": "Web (Internet Search)"
        }

    # 📜 ========== PARLIAMENT MODE ==========
    docs = retriever.invoke(query)
    docs = clean_docs(docs)

    if not docs:
        return {
            "answer": (
                "The retrieved parliamentary records mostly contain "
                "administrative headers or tabular data rather than "
                "descriptive discussion. Therefore, no detailed summary "
                "is available for this question."
            ),
            "source": "Parliamentary Records"
        }

    # Limit context size
    MAX_CHARS = 2500
    context = ""
    for text in docs:
        if len(context) < MAX_CHARS:
            context += text[:800] + "\n"

    # Detect header-dominated data
    if context.count("Written Answers") > 3:
        return {
            "answer": (
                "The Rajya Sabha records retrieved for this query consist "
                "primarily of unstarred written questions and administrative "
                "entries, which do not contain detailed discussion or debate. "
                "As a result, a substantive analytical answer cannot be generated."
            ),
            "source": "Parliamentary Records"
        }

    prompt = f"""
You are an expert analyst of Indian Parliamentary proceedings.

Based ONLY on the records below, answer the question in 3–5 clear bullet points.
Explain what was discussed, raised, or questioned.

DO NOT repeat the question.
DO NOT output headings only.
DO NOT output raw numbers or tables.

Parliamentary Records:
{context}

Question:
{query}

Answer:
"""

    answer = llm.invoke(prompt)

    return {
        "answer": answer.strip(),
        "source": "Parliamentary Records"
    }
