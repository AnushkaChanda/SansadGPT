\# 🏛️ SansadGPT



SansadGPT is a Retrieval-Augmented Generation (RAG) chatbot designed to answer

questions based on Indian Parliamentary records (Lok Sabha \& Rajya Sabha).

The system uses semantic search over parliamentary documents and automatically

falls back to web search for recent or time-sensitive queries.



---



\## 🔹 Key Features



\- 📄 Answers questions from Lok Sabha and Rajya Sabha records

\- 🔍 FAISS-based semantic retrieval over parliamentary PDFs

\- 🌐 Automatic web-search fallback for current information

\- 🧠 Open-source LLM (FLAN-T5) via HuggingFace

\- 🖥️ Interactive Streamlit interface

\- ✅ Responsible AI behavior (does not hallucinate when data is unavailable)



---



\## 🧩 Tech Stack



\- \*\*Python 3.11\*\*

\- \*\*LangChain\*\*

\- \*\*FAISS\*\*

\- \*\*HuggingFace Transformers\*\*

\- \*\*Sentence-Transformers\*\*

\- \*\*Streamlit\*\*

\- \*\*DuckDuckGo Search (ddgs)\*\*



---



\## ⚙️ How It Works



1\. User submits a query through the Streamlit UI

2\. The system checks if the query is time-sensitive

3\. If time-sensitive → performs web search

4\. Otherwise → retrieves relevant parliamentary records using FAISS

5\. The LLM generates a grounded answer based on retrieved context

6\. The source of the answer (Web or Parliamentary Records) is shown explicitly



---



\## 📌 Important Note on Parliamentary Data



Many Rajya Sabha and Lok Sabha records (especially \*Unstarred Questions\*)

are administrative or tabular in nature and do not contain debate-style

discussion or narrative explanations.



In such cases, SansadGPT \*\*explicitly informs the user\*\* that no substantive

discussion is available instead of generating speculative or fabricated answers.

This behavior is intentional and aligns with responsible AI principles.



---



\## ▶️ Running the Application



```bash

pip install -r requirements.txt

streamlit run app.py



