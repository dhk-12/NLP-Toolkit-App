# 🚀 AI-Powered NLP Toolkit Web App

An advanced **Natural Language Processing (NLP) Suite** built with **Streamlit**, **spaCy**, and **Hugging Face Transformers**.
This app provides high-performance NLP tools, including **Named Entity Recognition (NER)** and a **Dual-Mode Text Summarizer** (Traditional & AI-based).

---

## ✨ Features

### 1️⃣ Named Entity Recognition (NER)
* **Deep Analysis**: Detects and highlights entities in English text.
* **Categories**: Automatically identifies People, Locations, Organizations, Dates, and more.
* **Visual Interface**: Uses **spaCy's DisplaCy** for beautiful, interactive entity rendering.

### 2️⃣ Dual-Mode Text Summarization (New! ⚡)
Now supports two types of summarization to fit all needs:
* **Abstractive Summarization (AI)**: Uses the state-of-the-art **BART (Large-CNN)** model to understand the context and rewrite a human-like summary.
* **Extractive Summarization (Statistical)**: Offers multiple classic algorithms:
    * **LSA, Luhn, LexRank, and TextRank**.
* **Full Control**: Adjustable summary length (sentences for extractive / word count for BART).

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – Modern Web UI.
* **spaCy** – Industrial-strength NLP.
* **Hugging Face (Transformers)** – BART model for Abstractive Summarization.
* **Sumy** – Statistical summarization library.
* **PyTorch** – Deep learning backend.

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone [https://github.com/dhk-12/NLP-Toolkit-App.git]
cd NLP-Toolkit-App

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt

### 3️⃣ Run the application
```bash
streamlit run app.py

---

## 📷 App Modules

| Feature | Technology | Description |
| :--- | :--- | :--- |
| **NER Analysis** | spaCy (en_core_web_sm) | Visual extraction of named entities. |
| **AI Summarization** | BART (Abstractive) | Generates new sentences to summarize text. |
| **Classic Summarization**| LSA / TextRank (Extractive) | Selects the most important original sentences. |

---

## 👨‍💻 Author

Developed by **Hossam Khaled**

> **Note**: The first time you run the AI Summarizer, the app will download the BART model (~1.6GB). Subsequent runs will be much faster due to local caching.

If you find this toolkit useful, please give it a ⭐ on GitHub!