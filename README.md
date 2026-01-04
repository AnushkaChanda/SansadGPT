<div align="center">

# 🏛️ SansadGPT  
### Indian Parliament Question–Answer Chatbot

A Retrieval-Augmented Generation (RAG) system for querying  
Lok Sabha & Rajya Sabha parliamentary records with web fallback.

</div>

---

## 📖 Overview

**SansadGPT** is a Retrieval-Augmented Generation (RAG) chatbot designed to answer
natural-language questions using **Indian Parliamentary records** from the
**Lok Sabha** and **Rajya Sabha**.

The system performs **semantic search over parliamentary documents** and
automatically **falls back to web search** for recent or time-sensitive queries,
while clearly indicating the **source of every answer**.

---

## ✨ Key Features

- 📄 Answers questions from **Lok Sabha & Rajya Sabha** records  
- 🔍 **FAISS-based semantic retrieval** over parliamentary PDFs  
- 🌐 **Automatic web-search fallback** for current information  
- 🧠 Open-source LLM (**FLAN-T5**) via HuggingFace  
- 🖥️ Clean and interactive **Streamlit UI**  
- ✅ **Responsible AI behavior** (no hallucinated answers)  
- 🏷️ Explicit **source attribution** (Parliamentary Records / Web)

---

## 🧩 Tech Stack

| Layer | Technology |
|------|-----------|
| Language | **Python 3.11** |
| LLM | **FLAN-T5 (HuggingFace)** |
| Retrieval | **FAISS** |
| Embeddings | Sentence-Transformers |
| Framework | **LangChain** |
| Web Search | DuckDuckGo (`ddgs`) |
| Interface | **Streamlit** |

---

## ⚙️ How It Works

1. The user submits a query through the Streamlit interface  
2. The system checks whether the query is **time-sensitive**  
3. **Time-sensitive queries** → web search is performed  
4. **Non-time-sensitive queries** → parliamentary records are retrieved using FAISS  
5. The LLM generates a **grounded, context-aware answer**  
6. The **source of the answer** is displayed clearly  

---

## 📌 Important Note on Parliamentary Data

Many Lok Sabha and Rajya Sabha records — especially **Unstarred Questions** —
are **administrative or tabular** in nature and do **not contain narrative
discussion or debate transcripts**.

In such cases, **SansadGPT explicitly informs the user** that no substantive
discussion is available instead of generating speculative or fabricated answers.

This design choice follows **responsible AI and research integrity principles**.

---

## ▶️ How to Run the Application

### Step 1: Clone the Repository
```bash
git clone https://github.com/AnushkaChanda/SansadGPT.git
cd SansadGPT
```

**### Step 2: Create a Virtual Environment**
python -m venv venv

**### Step 3: Activate the Virtual Environment**(On Windows)
Step 3: Activate the Virtual Environment

**### Step 4: Install Required Dependencies**
pip install -r requirements.txt

**### Step 5: Run the Streamlit Application**
streamlit run app.py

**### Step 6: Open the Application**
http://localhost:8501
