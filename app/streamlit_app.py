import streamlit as st
import joblib, os, re, string, nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

st.set_page_config(page_title="Email Spam Classifier", page_icon="🛡️", layout="centered")

@st.cache_resource
def load_model():
    m_path = "artifacts/models/spam_classifier_model.pkl"
    v_path = "artifacts/models/tfidf_vectorizer.pkl"
    if os.path.exists(m_path) and os.path.exists(v_path):
        return joblib.load(m_path), joblib.load(v_path)
    return None, None

model, vectorizer = load_model()
stemmer = PorterStemmer()
try:
    stop_words = set(stopwords.words("english"))
except Exception:
    nltk.download("stopwords", quiet=True)
    stop_words = set(stopwords.words("english"))

def clean(text):
    text = str(text).lower()
    text = re.sub(r"https?://\S+|www\.\S+", " httpaddr ", text)
    text = re.sub(r"[\$\u00A3\u20AC\u00A5]", " currval ", text)
    text = re.sub(r"\b\d+\b", " numtoken ", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    return " ".join([stemmer.stem(w) for w in text.split() if w not in stop_words])

st.title("🛡️ Email Spam Detection AI")
st.markdown("**Sreyas Institute of Engineering & Technology** | Department of CSE (AI & ML)")
st.markdown("---")

txt = st.text_area("Enter email message body to analyze:", height=140, placeholder="e.g., Congratulations! You have won a $1,000 cash prize...")
if st.button("🔍 Check Email", use_container_width=True):
    if not txt.strip():
        st.warning("Please enter text to classify.")
    elif model is None:
        st.error("Model artifacts not yet generated. Run 'python scripts/train.py' first.")
    else:
        cl = clean(txt)
        vec = vectorizer.transform([cl])
        pred = model.predict(vec)[0]
        prob = model.predict_proba(vec)[0][1] * 100 if hasattr(model, "predict_proba") else 100.0
        if pred == 1:
            st.error(f"🚨 **SPAM DETECTED** (Spam Confidence: {prob:.1f}%)")
        else:
            st.success(f"✅ **HAM / LEGITIMATE EMAIL** (Spam Risk: {prob:.1f}%)")
