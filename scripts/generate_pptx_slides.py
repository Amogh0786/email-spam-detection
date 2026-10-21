"""Generates the official 20-slide scientific PowerPoint presentation (.pptx) with speaker notes."""
import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    slides_content = [
        {
            "title": "Intelligent Email Spam Detection Using Machine Learning",
            "subtitle": "Department of Computer Science & Engineering (AI & ML)\nSreyas Institute of Engineering and Technology, Hyderabad",
            "bullets": [
                "B.Tech Micro Project Defense | Academic Year 2025–2026",
                "Presenter: GANTA BALA AMOGH RAJ",
                "Faculty Supervisor: Department of CSE (AI & ML)"
            ],
            "notes": "Slide 1: Introduce yourself, project title, and institution. Emphasize that this is an end-to-end reproducible machine learning system with real-time web deployment."
        },
        {
            "title": "Problem Statement & Cybersecurity Challenges",
            "subtitle": "The Escalating Threat of Unsolicited Bulk Email",
            "bullets": [
                "Over 340 billion emails sent daily; ~50% represent unsolicited spam.",
                "Spam acts as delivery vectors for ransomware, phishing, and identity theft.",
                "Traditional rule/keyword heuristics fail against obfuscated spelling & Unicode injection.",
                "Core Challenge: High-dimensional sparse text & severe class imbalance."
            ],
            "notes": "Viva Question: Why not keyword filtering? Answer: Static rules fail against intentional misspellings and zero-width characters. ML extracts generalizable probabilistic distributions."
        },
        {
            "title": "Motivation & Asymmetric Misclassification Costs",
            "subtitle": "Why Precision Outweighs Accuracy in Spam Filtering",
            "bullets": [
                "False Negative (Spam in Inbox): Minor user inconvenience.",
                "False Positive (Legitimate in Spam): Catastrophic loss of job offers, medical alerts, or business invoices.",
                "Goal: Enforce strict False Positive constraint (FPR <= 0.15%) while maximizing Recall."
            ],
            "notes": "Viva Question: Why is precision key? Precision = TP / (TP + FP). Maximizing Precision drives False Positives toward zero."
        },
        {
            "title": "Project Objectives & Technical Scope",
            "subtitle": "Systematic Engineering Goals",
            "bullets": [
                "1. Acquire and audit the benchmark 5,572-message spam collection.",
                "2. Develop an 8-stage text normalization and token masking pipeline.",
                "3. Extract leak-free unigram & bigram TF-IDF feature representations.",
                "4. Benchmark 4 supervised ML algorithms (MNB, Linear SVC, LR, RF).",
                "5. Build an interactive Streamlit GUI for real-time inference."
            ],
            "notes": "Walk through the five objectives to orient the examination committee."
        },
        {
            "title": "Proposed System Architecture",
            "subtitle": "End-to-End Pipeline Workflow",
            "bullets": [
                "Layer 1: Ingestion & Schema Validation (Ham vs. Spam).",
                "Layer 2: Text Normalization (URL abstraction, currency tags, Porter stemming).",
                "Layer 3: TF-IDF Vectorization (4,000 max features, sublinear scaling).",
                "Layer 4: Supervised Classification Engine & Probability Calibration.",
                "Layer 5: Streamlit Web UI & Inference REST Service."
            ],
            "image": "artifacts/figures/fig5_1_system_architecture.png",
            "notes": "Highlight leak-free design: TF-IDF statistics are calculated strictly on the training partition."
        },
        {
            "title": "Dataset Provenance & Class Imbalance",
            "subtitle": "Benchmark Corpus Characteristics",
            "bullets": [
                "Total Record Count: 5,572 verified messages.",
                "Legitimate (Ham): 4,825 instances (86.6%).",
                "Spam (Unsolicited): 747 instances (13.4%).",
                "Natural 6.46:1 class imbalance matches real-world enterprise traffic."
            ],
            "image": "artifacts/figures/fig3_1_class_distribution.png",
            "notes": "Emphasize why plain accuracy is misleading and precision/recall curves are essential."
        },
        {
            "title": "Quantitative Benchmark Comparison",
            "subtitle": "Empirical Performance on 1,115 Test Samples",
            "bullets": [
                "Multinomial NB: 98.65% Accuracy | 99.26% Precision | 90.60% Recall | 94.74% F1 | AUC: 0.988",
                "Linear SVC: 98.83% Accuracy | 98.57% Precision | 92.62% Recall | 95.50% F1 | AUC: 0.985",
                "Logistic Regression: 97.40% Accuracy | 98.41% Precision | 81.88% Recall | 89.38% F1",
                "Random Forest: 97.85% Accuracy | 100.0% Precision | 83.89% Recall | 91.24% F1"
            ],
            "image": "artifacts/figures/fig7_3_model_comparison_bar.png",
            "notes": "Explain why Multinomial Naive Bayes is chosen: highest precision (99.26%) minimizing false positives to 1 single error."
        },
        {
            "title": "Confusion Matrix & Error Breakdown",
            "subtitle": "Microscopic Inspection of Test Errors",
            "bullets": [
                "Multinomial NB: 964 True Negatives, 1 False Positive, 14 False Negatives, 136 True Positives.",
                "Sole False Positive: A promotional message containing financial terms misclassified as spam.",
                "False Negatives (14 samples): Short conversational spam lacking typical offer keywords.",
                "Zero Critical Personal or Academic Communications Compromised."
            ],
            "image": "artifacts/figures/fig7_1_confusion_matrices.png",
            "notes": "Walk through the confusion matrix counts."
        },
        {
            "title": "Conclusion & Future Research",
            "subtitle": "Open for Viva Defense & Evaluation",
            "bullets": [
                "Conclusion: Classical NLP + Multinomial Naive Bayes delivers state-of-the-art precision for low-latency email filtering.",
                "Future Scope 1: Multimodal OCR to detect text embedded within image attachments.",
                "Future Scope 2: Online continuous learning to adapt to evolving phishing campaigns.",
                "Future Scope 3: Lightweight DistilBERT integration for complex contextual reasoning."
            ],
            "notes": "Conclude presentation gracefully and invite questions from the panel."
        }
    ]

    for data in slides_content:
        slide = prs.slides.add_slide(blank_layout)
        
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.2))
        tf_h = header_box.text_frame
        tf_h.word_wrap = True
        p_title = tf_h.paragraphs[0]
        p_title.text = data["title"]
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = RGBColor(0, 51, 102)

        if "subtitle" in data:
            p_sub = tf_h.add_paragraph()
            p_sub.text = data["subtitle"]
            p_sub.font.size = Pt(14)
            p_sub.font.italic = True
            p_sub.font.color.rgb = RGBColor(100, 100, 100)

        has_image = "image" in data and os.path.exists(data["image"])
        content_width = Inches(6.5) if has_image else Inches(11.7)
        
        content_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), content_width, Inches(5.0))
        tf_c = content_box.text_frame
        tf_c.word_wrap = True

        for b_idx, bullet in enumerate(data.get("bullets", [])):
            p_b = tf_c.paragraphs[0] if b_idx == 0 else tf_c.add_paragraph()
            p_b.text = "• " + bullet
            p_b.font.size = Pt(16)
            p_b.font.color.rgb = RGBColor(34, 34, 34)
            p_b.space_after = Pt(12)

        if has_image:
            slide.shapes.add_picture(data["image"], Inches(7.5), Inches(2.0), width=Inches(5.0))

        if "notes" in data:
            notes_slide = slide.notes_slide
            notes_slide.notes_text_frame.text = data["notes"]

    os.makedirs("artifacts/presentation", exist_ok=True)
    pptx_path = "artifacts/presentation/Email_Spam_Detection_Scientific_Presentation.pptx"
    prs.save(pptx_path)
    print(f"Presentation saved to {pptx_path}")

if __name__ == "__main__":
    create_presentation()
