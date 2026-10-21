import joblib, os
from src.preprocessing.text_preprocessor import TextPreprocessor

class SpamInferenceService:
    def __init__(self, model_path="artifacts/models/spam_classifier_model.pkl",
                 vectorizer_path="artifacts/models/tfidf_vectorizer.pkl"):
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)
        self.preprocessor = TextPreprocessor()

    def predict(self, raw_message: str):
        cleaned = self.preprocessor.clean_text(raw_message)
        features = self.vectorizer.transform([cleaned])
        pred = self.model.predict(features)[0]
        prob = self.model.predict_proba(features)[0][1] * 100 if hasattr(self.model, "predict_proba") else (100.0 if pred == 1 else 0.0)
        return {"label": "Spam" if pred == 1 else "Ham", "is_spam": bool(pred == 1), "confidence": round(prob, 2)}
