"""Master training script."""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json, joblib, pandas as pd
from sklearn.model_selection import train_test_split
from src.preprocessing.text_preprocessor import TextPreprocessor
from src.features.feature_builder import FeatureBuilder
from src.models.model_factory import get_models
from src.evaluation.evaluator import ModelEvaluator

def run():
    print("Loading dataset...")
    data_path = "artifacts/data/spam.csv"
    if not os.path.exists(data_path):
        os.makedirs(os.path.dirname(data_path), exist_ok=True)
        import urllib.request
        url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
        df = pd.read_csv(url, sep="\t", header=None, names=["label", "message"])
        df.to_csv(data_path, index=False)
    else:
        df = pd.read_csv(data_path)

    df["label_num"] = df["label"].map({"ham": 0, "spam": 1})
    prep = TextPreprocessor()
    df["clean"] = prep.transform_series(df["message"])

    X_train, X_test, y_train, y_test = train_test_split(
        df["clean"], df["label_num"], test_size=0.20, random_state=42, stratify=df["label_num"]
    )

    fb = FeatureBuilder(max_features=4000, ngram_range=(1, 2))
    X_train_vec = fb.fit_transform(X_train)
    X_test_vec = fb.transform(X_test)

    models = get_models()
    results = {}
    best_score = -1
    best_model = None

    for name, model in models.items():
        print(f"Training {name}...")
        model.fit(X_train_vec, y_train)
        res = ModelEvaluator.evaluate(model, X_test_vec, y_test, model_name=name)
        results[name] = res
        score = res["precision"] * 0.6 + res["f1_score"] * 0.4
        if score > best_score:
            best_score = score
            best_model = model

    os.makedirs("artifacts/models", exist_ok=True)
    os.makedirs("artifacts/metrics", exist_ok=True)
    fb.save("artifacts/models/tfidf_vectorizer.pkl")
    joblib.dump(best_model, "artifacts/models/spam_classifier_model.pkl")
    with open("artifacts/metrics/evaluation_results.json", "w") as f:
        json.dump(results, f, indent=4)
    print("Training complete! Artifacts saved.")

if __name__ == "__main__":
    run()
