# NLP Toolkit Web App

A simple **Natural Language Processing (NLP) Web Application** built with **Streamlit**, **spaCy**, and **Sumy**.
The app provides useful NLP tools such as **Named Entity Recognition (NER)** and **Text Summarization** through a simple and interactive web interface.

---

## 🚀 Features

### 1️⃣ Named Entity Recognition (NER)

* Detects entities in English text.
* Identifies:

  * People
  * Locations
  * Organizations
  * Dates
  * Other named entities
* Uses **spaCy NLP model**.

### 2️⃣ Text Summarization

* Automatically summarizes long text.
* Multiple summarization algorithms:

  * LSA
  * Luhn
  * LexRank
  * TextRank
* Adjustable number of summary sentences.

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – Web interface
* **spaCy** – NLP processing
* **Sumy** – Text summarization algorithms
* **NLTK** – Tokenization support

---

## 📦 Installation

### 1️⃣ Clone the repository

bash
git clone https://github.com/your-username/NLP-Toolkit-App.git
cd NLP-Toolkit-App


### 2️⃣ Install dependencies

bash
pip install -r requirements.txt

### 3️⃣ Download spaCy language model

bash
python -m spacy download en_core_web_sm


---

## ▶️ Run the App

Start the Streamlit application:

streamlit run app.py

Then open the browser at:

http://localhost:8501

---

## 📷 App Interface

The application contains two main tools:

| Tool                     | Description                              |
| ------------------------ | ---------------------------------------- |
| Named Entity Recognition | Detects entities in text                 |
| Text Summarization       | Generates a short summary from long text |

---

## 📁 Project Structure

NLP-Toolkit-App
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

---

## 💡 Example Use Cases

* Analyzing text documents
* Extracting entities from articles
* Summarizing long reports
* NLP learning and experimentation

---

## 📈 Future Improvements

Possible features to add:

* Sentiment Analysis
* Keyword Extraction
* Language Detection
* Multi-language support
* File upload (PDF / TXT)

---

## 👨‍💻 Author

Developed by **Hossam Khaled**

If you like this project, consider giving it a ⭐ on GitHub.
