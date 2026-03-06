import nltk
import spacy
import streamlit as st
from spacy import displacy
from transformers import pipeline
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer

st.set_page_config(page_title="NLP Web App", layout="wide")

@st.cache_resource
def download_assets():
    nltk.download('punkt')

@st.cache_resource
def load_spacy_model():
    return spacy.load("en_core_web_sm")

@st.cache_resource
def load_bart_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

download_assets()
nlp = load_spacy_model()
bart_summarizer = load_bart_summarizer()

def summarize(text, summarizer_type, sentence_count, max_len, min_len):
    if summarizer_type == "bart":
        summary = bart_summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
        return summary[0]['summary_text']
    
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    if summarizer_type == "lsa":
        summarizer = LsaSummarizer()
    elif summarizer_type == "luhn":
        summarizer = LuhnSummarizer()
    elif summarizer_type == "lexrank":
        summarizer = LexRankSummarizer()
    elif summarizer_type == "textrank":
        summarizer = TextRankSummarizer()
    
    summary_sentences = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary_sentences)

def main():
    st.title("NLP Web App")

    tab1, tab2 = st.tabs(["Named Entity Recognition", "Text Summarization"])

    with tab1:
        st.header("Named Entity Recognition (NER)")
        st.write("Enter some **English** text to identify named entities.")
        text_ner = st.text_area("Input Text", key="ner_input", height=150)
        
        if st.button("Analyze Entities"):
            if text_ner:
                doc = nlp(text_ner)
                html = displacy.render(doc, style="ent", page=False)
                st.write(html, unsafe_allow_html=True)
            else:
                st.warning("Please Input Text first")

    with tab2:
        st.header("Text Summarization")
        st.write("Choose between traditional (Extractive) or AI-based (Abstractive) summarization.")
        
        text_sum = st.text_area("Please enter some text", key="sum_input", height=150)

        col1, col2 = st.columns(2)
        with col1:
            summarizer_type = st.selectbox(
                "Choose Summarizer", 
                ("lsa", "luhn", "lexrank", "textrank", "bart")
            )
        with col2:
            if summarizer_type == "bart":
                max_len = st.slider("Max Length", 50, 500, 130)
                min_len = st.slider("Min Length", 10, 150, 30)
                sentence_count = None
            else:
                sentence_count = st.slider("Number of Sentences", 1, 10, 4)
                max_len, min_len = None, None

        if st.button("Summarize"):
            if text_sum:
                with st.spinner("Processing..."):
                    result = summarize(text_sum, summarizer_type, sentence_count, max_len, min_len)
                    st.subheader("Summary Result:")
                    st.success(result)
            else:
                st.warning("Please enter some text to summarize.")

if __name__ == "__main__":
    main()