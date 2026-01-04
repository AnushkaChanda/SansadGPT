<div align="center">

# 🏛️ **SansadGPT**
### *Indian Parliament Question–Answer Chatbot*

A **Retrieval-Augmented Generation (RAG)** system for answering questions from  
**Lok Sabha & Rajya Sabha parliamentary records**, with intelligent web fallback.

</div>

---

## 📖 Overview

**SansadGPT** is an AI-powered chatbot that enables users to ask natural-language questions about Indian Parliamentary proceedings.

It performs **semantic search over official parliamentary documents** and, when required, **automatically switches to web search** for recent or time-sensitive queries — always showing **where the answer comes from**.

---

## ✨ Key Features

- 🏛️ **Parliamentary QA**  
  Answers questions using Lok Sabha & Rajya Sabha records

- 🔍 **Semantic Retrieval**  
  FAISS-powered vector search over parliamentary PDFs

- 🌐 **Web Fallback**  
  Automatically searches the internet for current or missing information

- 🧠 **Open-Source LLM**  
  Uses **FLAN-T5** via HuggingFace (no closed APIs)

- 🖥️ **Interactive UI**  
  Clean Streamlit-based question–answer interface

- ✅ **Responsible AI**  
  Clearly states when no substantive information is available  
  *(no hallucinated answers)*

---

## 🧩 Tech Stack

| Layer | Technology |
|-----|-----------|
| Language | **Python 3.11** |
| LLM | **FLAN-T5 (HuggingFace)** |
| Retrieval | **FAISS** |
| Embeddings | Sentence-Transformers |
| Framework | **LangChain** |
| Web Search | DuckDuckGo (`ddgs`) |
| Interface | **Streamlit** |

---

## ⚙️ How It Works

```text
User Query
   ↓
Time-Sensitivity Check
   ├── Yes → 🌐 Web Search
   └── No  → 📚 FAISS Retrieval
                ↓
           Context-Grounded LLM Answer
                ↓
        Answer + Source Attribution
