# 🛡️ Intelligent Email Spam Detection Using Machine Learning & NLP

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Streamlit App](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)
[![Institution](https://img.shields.io/badge/Institution-Sreyas%20SIET%20(CSE--AIML)-orange.svg)](https://sreyas.ac.in/)

> **Academic Micro Project** submitted to the **Department of Computer Science and Engineering (Artificial Intelligence & Machine Learning)**, Sreyas Institute of Engineering and Technology (Autonomous), Hyderabad.

---

## 📌 Project Overview
Unsolicited electronic mail (spam) represents over 50% of global daily email transmissions, acting as a primary delivery mechanism for phishing, financial fraud, and malware. 

This project provides an end-to-end, reproducible machine learning framework for binary email spam classification. Because misclassifying a legitimate email (False Positive) incurs high cost, the system is optimized for **maximum precision** while preserving sub-millisecond inference latency.

---

## 🚀 Key Results & Highlights
- **Champion Classifier:** Multinomial Naive Bayes ($\alpha = 0.2$)
- **Accuracy:** `98.65%`
- **Spam Precision:** `99.26%` *(Only 1 False Positive out of 965 legitimate test messages; $\text{FPR} = 0.10\%$)*
- **ROC-AUC Score:** `0.9880`
- **Inference Latency:** `< 0.1 ms` per message
- **Interactive UI:** Real-time classification via Streamlit

---

## 📊 Benchmark Model Comparison

| Algorithm | Accuracy | Precision (Spam) | Recall (Spam) | F1-Score | ROC-AUC | False Positives |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Multinomial Naive Bayes** | **98.65%** | **99.26%** | **90.60%** | **94.74%** | **0.9880** | **1** |
| **Linear Support Vector Classifier** | 98.83% | 98.57% | 92.62% | 95.50% | 0.9850 | 2 |
| **Logistic Regression** | 97.40% | 98.41% | 81.88% | 89.38% | 0.9810 | 2 |
| **Random Forest Ensemble** | 97.85% | 100.00% | 83.89% | 91.24% | 0.9790 | 0 |

---

## ⚡ Quickstart

```bash
# 1. Clone repository
git clone https://github.com/Amogh0786/email-spam-detection.git
cd email-spam-detection

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run unit tests
pytest tests/ -v

# 4. Train model
python scripts/train.py

# 5. Generate figures and reports
python scripts/generate_figures.py
python scripts/generate_docx_report.py
python scripts/generate_pptx_slides.py

# 6. Launch interactive web app
streamlit run app/streamlit_app.py
```

---

## 📁 Repository Structure
```
email-spam-detection/
├── app/                  # Streamlit web application
├── artifacts/            # Generated models, figures, metrics, reports & PPT
│   ├── figures/          # High-resolution publication plots
│   ├── models/           # Serialized model & vectorizer pickles
│   ├── presentation/     # 20-slide scientific presentation (.pptx)
│   └── reports/          # Sreyas HOD-compliant micro project report (.docx)
├── config/               # Centralized hyperparameters & settings
├── notebooks/            # Self-contained Google Colab notebook (.ipynb)
├── scripts/              # Training, evaluation & document generation scripts
├── src/                  # Production Python package (data, preprocessing, models)
├── tests/                # Automated unit tests
├── requirements.txt      # Project dependencies
└── README.md
```

---

## 👤 Author & Attribution
- **Student Name:** GANTA BALA AMOGH RAJ
- **GitHub:** [@Amogh0786](https://github.com/Amogh0786)
- **Email:** [balaamoghraj@gmail.com](mailto:balaamoghraj@gmail.com)
- **Department:** Computer Science & Engineering (AI & ML)
- **Institution:** Sreyas Institute of Engineering and Technology, Hyderabad
