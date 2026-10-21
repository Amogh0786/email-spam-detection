"""Text preprocessing and cleaning pipeline for email messages."""
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

class TextPreprocessor:
    def __init__(self, use_stemming=True, remove_stopwords=True):
        self.use_stemming = use_stemming
        self.remove_stopwords = remove_stopwords
        self.stemmer = PorterStemmer() if use_stemming else None
        self.stop_words = set(stopwords.words('english')) if remove_stopwords else set()
        self.stop_words.discard('free')
        self.stop_words.discard('win')
        self.stop_words.discard('urgent')

    def clean_text(self, text: str) -> str:
        if not isinstance(text, str):
            return ""
        text = text.lower()
        text = re.sub(r'https?://\S+|www\.\S+', ' httpaddr ', text)
        text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', ' emailaddr ', text)
        # Currency symbols: dollar, pound, euro, yen
        text = re.sub(r'[\$\u00A3\u20AC\u00A5]', ' currval ', text)
        text = re.sub(r'\b\d+\b', ' numtoken ', text)
        text = re.sub(r'<.*?>', ' ', text)
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = text.split()
        if self.remove_stopwords:
            tokens = [w for w in tokens if w not in self.stop_words]
        if self.use_stemming:
            tokens = [self.stemmer.stem(w) for w in tokens]
        return " ".join(tokens)

    def transform_series(self, series):
        return series.apply(self.clean_text)
