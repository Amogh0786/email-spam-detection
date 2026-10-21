from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import os

class FeatureBuilder:
    def __init__(self, max_features=4000, ngram_range=(1, 2), sublinear_tf=True, min_df=1):
        self.vectorizer = TfidfVectorizer(
            max_features=max_features,
            ngram_range=ngram_range,
            sublinear_tf=sublinear_tf,
            min_df=min_df,
            lowercase=False
        )

    def fit_transform(self, texts):
        return self.vectorizer.fit_transform(texts)

    def transform(self, texts):
        return self.vectorizer.transform(texts)

    def save(self, filepath: str):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        joblib.dump(self.vectorizer, filepath)

    @classmethod
    def load(cls, filepath: str):
        inst = cls()
        inst.vectorizer = joblib.load(filepath)
        return inst
