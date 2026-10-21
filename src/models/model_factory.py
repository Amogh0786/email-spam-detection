from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier

def get_models():
    return {
        "Multinomial Naive Bayes": MultinomialNB(alpha=0.2),
        "Linear Support Vector Classifier": LinearSVC(C=0.8, random_state=42),
        "Logistic Regression": LogisticRegression(C=1.5, max_iter=1000, solver='liblinear', random_state=42),
        "Random Forest Classifier": RandomForestClassifier(n_estimators=150, max_depth=25, random_state=42)
    }
