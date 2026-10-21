import pytest
from src.preprocessing.text_preprocessor import TextPreprocessor
from src.features.feature_builder import FeatureBuilder
from src.models.model_factory import get_models

def test_preprocessor_masking():
    p = TextPreprocessor()
    text = "Win $500 cash! Visit https://win.com now"
    cleaned = p.clean_text(text)
    assert "currval" in cleaned
    assert "httpaddr" in cleaned

def test_tfidf_extraction():
    fb = FeatureBuilder(max_features=100)
    matrix = fb.fit_transform(["Hello world email", "Win lottery prize"])
    assert matrix.shape[0] == 2

def test_models_exist():
    m = get_models()
    assert "Multinomial Naive Bayes" in m
