"""Populates student identities, roll numbers, team roles, certificate, declaration,
module contributions, individual assessment, and reflections across all project documentation and presentation.
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import docx
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def set_cell(cell, text, bold=False, font_size=9.5, align=WD_ALIGN_PARAGRAPH.LEFT):
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = align
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(font_size)
    run.bold = bold

def update_team_details():
    doc_path = "ML-Project Documentation_Updated.docx"
    doc = Document(doc_path)
    print("Opened ML-Project Documentation_Updated.docx...")

    # ==================== 1. COVER PAGE PARAGRAPHS ====================
    # Title
    if len(doc.paragraphs) > 3:
        p3 = doc.paragraphs[3]
        p3.text = "EMAIL SPAM DETECTION"
        p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p3.runs:
            r.font.name = "Times New Roman"
            r.font.size = Pt(18)
            r.bold = True
            r.font.color.rgb = RGBColor(0, 51, 102)

    # Course details
    if len(doc.paragraphs) > 5:
        p5 = doc.paragraphs[5]
        p5.text = "Course: Machine Learning (CSE - AI & ML)"
        p5.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p5.runs:
            r.font.name = "Times New Roman"
            r.font.size = Pt(12)
            r.bold = True

    # ==================== 2. TABLE 0: SUBMITTED BY (TEAM DETAILS) ====================
    t0 = doc.tables[0]
    set_cell(t0.cell(1, 0), "1", align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(t0.cell(1, 1), "24VE1A6681", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(t0.cell(1, 2), "GANTA BALA AMOGH RAJ", bold=True)
    set_cell(t0.cell(1, 3), "Team Lead & ML Architect")

    set_cell(t0.cell(2, 0), "2", align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(t0.cell(2, 1), "24VE1A6677", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(t0.cell(2, 2), "DOMA AJAY", bold=True)
    set_cell(t0.cell(2, 3), "Team Member & Data/Preprocessing Analyst")

    # Clear empty placeholder rows 3 and 4
    if len(t0.rows) > 3:
        for c in t0.rows[3].cells:
            c.text = ""
    if len(t0.rows) > 4:
        for c in t0.rows[4].cells:
            c.text = ""

    # ==================== 3. CERTIFICATE SECTION ====================
    # Certificate Table 1
    t1 = doc.tables[1]
    set_cell(t1.cell(1, 0), "1", align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(t1.cell(1, 1), "24VE1A6681", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(t1.cell(1, 2), "GANTA BALA AMOGH RAJ", bold=True)

    set_cell(t1.cell(2, 0), "2", align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(t1.cell(2, 1), "24VE1A6677", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(t1.cell(2, 2), "DOMA AJAY", bold=True)

    if len(t1.rows) > 3:
        for c in t1.rows[3].cells:
            c.text = ""
    if len(t1.rows) > 4:
        for c in t1.rows[4].cells:
            c.text = ""

    # Certificate Paragraph (P17)
    if len(doc.paragraphs) > 17:
        p17 = doc.paragraphs[17]
        p17.text = ("This is to certify that the micro project entitled 'EMAIL SPAM DETECTION' is a bonafide work "
                    "carried out by GANTA BALA AMOGH RAJ (Roll No: 24VE1A6681) and DOMA AJAY (Roll No: 24VE1A6677), "
                    "students of B.Tech, Department of CSE (Artificial Intelligence & Machine Learning), Sreyas Institute "
                    "of Engineering and Technology, in partial fulfilment of the requirements of the course Machine Learning "
                    "during the academic year 2025–2026. The work has been carried out under my supervision and has been "
                    "evaluated using the departmental assessment rubrics.")
        p17.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        for r in p17.runs:
            r.font.name = "Times New Roman"
            r.font.size = Pt(12)

    # ==================== 4. DECLARATION SECTION ====================
    # Declaration Table 3
    t3 = doc.tables[3]
    set_cell(t3.cell(1, 0), "1", align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(t3.cell(1, 1), "24VE1A6681", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(t3.cell(1, 2), "GANTA BALA AMOGH RAJ", bold=True)
    set_cell(t3.cell(1, 3), "[Signature]", align=WD_ALIGN_PARAGRAPH.CENTER)

    set_cell(t3.cell(2, 0), "2", align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(t3.cell(2, 1), "24VE1A6677", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(t3.cell(2, 2), "DOMA AJAY", bold=True)
    set_cell(t3.cell(2, 3), "[Signature]", align=WD_ALIGN_PARAGRAPH.CENTER)

    if len(t3.rows) > 3:
        for c in t3.rows[3].cells:
            c.text = ""
    if len(t3.rows) > 4:
        for c in t3.rows[4].cells:
            c.text = ""

    # Declaration Paragraph (P22)
    if len(doc.paragraphs) > 22:
        p22 = doc.paragraphs[22]
        p22.text = ("We hereby declare that the micro project report entitled 'EMAIL SPAM DETECTION' submitted to the "
                    "Department of CSE (AI & ML), Sreyas Institute of Engineering and Technology, is a record of original work "
                    "done by us under the guidance of our faculty guide. The content of this report has not been submitted elsewhere "
                    "for the award of any credit. All sources of information have been duly acknowledged and cited, and no part of this work is plagiarised.")
        p22.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        for r in p22.runs:
            r.font.name = "Times New Roman"
            r.font.size = Pt(12)

    # ==================== 5. TABLE 35: TASK ALLOCATION & CONTRIBUTIONS ====================
    t35 = doc.tables[35]
    contrib = [
        ("1", "Dataset collection, cleaning & EDA", 
         "Acquired benchmark 5,572 corpus, audited class imbalance, computed dispersion statistics, and rendered frequency distributions.", 
         "DOMA AJAY (24VE1A6677)"),
        ("2", "NLP Preprocessing & Feature Engineering", 
         "Implemented 8-stage text normalization pipeline, URL/currency regex masking, stopword removal, Porter stemming, and TF-IDF extraction.", 
         "DOMA AJAY (24VE1A6677)"),
        ("3", "Model Training, Cross-Validation & Tuning", 
         "Configured and trained Multinomial Naive Bayes, Linear SVC, Logistic Regression, and Random Forest models with 5-fold CV and grid search.", 
         "GANTA BALA AMOGH RAJ (24VE1A6681)"),
        ("4", "Evaluation, Error Analysis, Web GUI & Docs", 
         "Evaluated cost-sensitive precision metrics, generated confusion matrices, deployed Streamlit interface, and authored micro project report.", 
         "GANTA BALA AMOGH RAJ (24VE1A6681)")
    ]
    for r_idx, row in enumerate(contrib, start=1):
        for c_idx, val in enumerate(row):
            set_cell(t35.cell(r_idx, c_idx), val, bold=(c_idx in [0, 3]))

    # ==================== 6. TABLE 46: INDIVIDUAL ASSESSMENT SHEET ====================
    t46 = doc.tables[46]
    set_cell(t46.cell(1, 0), "24VE1A6681", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(t46.cell(1, 1), "GANTA BALA AMOGH RAJ", bold=True)

    set_cell(t46.cell(2, 0), "24VE1A6677", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(t46.cell(2, 1), "DOMA AJAY", bold=True)

    # ==================== 7. TABLE 48: REFLECTION - TEAM LEAD ====================
    t48 = doc.tables[48]
    refl_lead = [
        ("Which ML concepts did I understand best through this project?", 
         "I gained a deep, mathematical understanding of how high-dimensional text is vectorized via sublinear TF-IDF, how Laplace smoothing prevents zero-probability collapse in Naive Bayes, and why Spam Precision must be prioritized over generic accuracy in cost-asymmetric classification problems."),
        ("What was the hardest problem I faced, and how did I solve it?", 
         "The most challenging problem was minimizing False Positives (preventing legitimate emails from dropping into spam) while preserving high Spam Recall. I addressed this by establishing domain-specific meta-token masking and fine-tuning the Naive Bayes smoothing parameter alpha to 0.2."),
        ("If I had two more weeks, what would I add or improve?", 
         "I would evaluate lightweight distilled transformers such as DistilBERT to test whether contextual attention improves short conversational spam detection, and construct an Optical Character Recognition (OCR) pipeline for image attachments."),
        ("How did our team divide the work, and was it effective?", 
         "The division of responsibilities was highly effective: Doma Ajay handled dataset acquisition, exploratory data analysis, and the 8-stage text preprocessing pipeline, while I led model training, hyperparameter optimization, error analysis, and Streamlit deployment.")
    ]
    for r_idx, (q, r) in enumerate(refl_lead, start=1):
        set_cell(t48.cell(r_idx, 0), q, bold=True)
        set_cell(t48.cell(r_idx, 1), r)

    # ==================== 8. TABLE 49: REFLECTION - TEAM MEMBER ====================
    t49 = doc.tables[49]
    refl_member = [
        ("Which ML concepts did I understand better through this project?", 
         "I gained practical mastery of natural language text processing, tokenization, regular expression masking (converting URLs, currencies, and numbers to standard meta-tokens), stopword elimination, and how TF-IDF vectorization maps text into dense numerical feature matrices."),
        ("What was the hardest problem (data, convergence, overfitting) and how was it solved?", 
         "The hardest problem was managing noise, irregular capitalization, and class imbalance in raw unstructured text. We solved this by implementing an 8-stage deterministic preprocessing pipeline and applying stratified shuffle splitting to maintain class proportions."),
        ("What new tool or library did I learn on my own?", 
         "I learned NLTK for morphological stemming (PorterStemmer) and Seaborn/Matplotlib for rendering publication-quality class distributions, confusion matrix heatmaps, and ROC curves."),
        ("What would I do differently next time?", 
         "Next time, I would explore n-gram ranges beyond bigrams (e.g., trigrams) and test WordNet lemmatization to evaluate whether preserving morphological word lemmas offers advantages over algorithmic stemming.")
    ]
    for r_idx, (q, r) in enumerate(refl_member, start=1):
        set_cell(t49.cell(r_idx, 0), q, bold=True)
        set_cell(t49.cell(r_idx, 1), r)

    # Save to ML-Project Documentation_Updated.docx
    doc.save("ML-Project Documentation_Updated.docx")
    print("Saved updated team details to ML-Project Documentation_Updated.docx!")

    # Save to artifacts/reports/
    os.makedirs("artifacts/reports", exist_ok=True)
    doc.save("artifacts/reports/ML_Project_Documentation_Email_Spam_Detection.docx")
    print("Saved to artifacts/reports/ML_Project_Documentation_Email_Spam_Detection.docx!")

    # Attempt to save directly to ML-Project Documentation.docx
    try:
        doc.save("ML-Project Documentation.docx")
        print("Successfully updated ML-Project Documentation.docx directly!")
    except Exception as e:
        print(f"Notice: ML-Project Documentation.docx is locked in Word ({e}). Updated version is saved in ML-Project Documentation_Updated.docx.")

def update_presentation():
    import pptx
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor

    pptx_path = "artifacts/presentation/Email_Spam_Detection_Scientific_Presentation.pptx"
    if not os.path.exists(pptx_path):
        return
    prs = Presentation(pptx_path)
    # Update Slide 1 (Title slide)
    slide1 = prs.slides[0]
    for shape in slide1.shapes:
        if shape.has_text_frame:
            tf = shape.text_frame
            for p in tf.paragraphs:
                if "Presenter:" in p.text or "GANTA BALA" in p.text:
                    p.text = "Presenters: GANTA BALA AMOGH RAJ (24VE1A6681) & DOMA AJAY (24VE1A6677)"
                    p.font.size = Pt(16)
                    p.font.color.rgb = RGBColor(0, 51, 102)
                    p.font.bold = True
    prs.save(pptx_path)
    print("Updated Slide 1 of presentation with both team members and roll numbers.")

if __name__ == "__main__":
    update_team_details()
    update_presentation()
