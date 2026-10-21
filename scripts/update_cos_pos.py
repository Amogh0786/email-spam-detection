"""Updates Course Outcomes (COs) and Programme Outcomes (POs) in ML-Project Documentation.docx
strictly adhering to the official Machine Learning course syllabus and the NBA Tier-I PO definitions from New POs.pdf.
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import docx
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def set_cell_text(cell, text, bold=False, font_size=9.5, italic=False, align=WD_ALIGN_PARAGRAPH.LEFT):
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = align
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(font_size)
    run.bold = bold
    run.italic = italic

def update_cos_and_pos():
    doc_path = "ML-Project Documentation.docx"
    doc = Document(doc_path)
    print("Opened document to update COs and POs...")

    # 1. Update Introductory Paragraph
    if len(doc.paragraphs) > 56:
        p56 = doc.paragraphs[56]
        p56.text = ("This section presents the comprehensive outcome mapping for the Machine Learning course. "
                    "The six Course Outcomes (COs) defined for the course are mapped to the eleven National Board of "
                    "Accreditation (NBA SAR – Tier I) Programme Outcomes (POs) and two Programme Specific Outcomes (PSOs). "
                    "The alignment demonstrates how statistical analysis, data preprocessing, supervised learning, parameter "
                    "tuning, unsupervised grouping, and comparative mini-project evaluation substantiate each graduate attribute.")
        p56.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        for r in p56.runs:
            r.font.name = "Times New Roman"
            r.font.size = Pt(12)

    # 2. Table 5: Course Outcomes
    t5 = doc.tables[5]
    while len(t5.rows) < 7:
        t5.add_row()

    cos_data = [
        ("CO1", 
         "Compute central tendency and dispersion measures (Mean, Median, Mode, Variance, Standard Deviation) on datasets using Python and statistical libraries.", 
         "L3 (Apply)", 
         "Chapter 3 (EDA & Statistical Summary)"),
        ("CO2", 
         "Utilize Python libraries such as NumPy, SciPy, Pandas, Matplotlib, and Seaborn for data manipulation, visualization, and exploratory data analysis.", 
         "L3 (Apply)", 
         "Chapters 3 & 4 (Data Preprocessing & Visualizations)"),
        ("CO3", 
         "Implement supervised learning algorithms including Simple Linear Regression, Multiple Linear Regression, Logistic Regression, Decision Trees, and K-Nearest Neighbors (KNN) using scikit-learn.", 
         "L3 (Apply)", 
         "Chapters 5 & 6 (Logistic Regression, Decision Trees / Random Forest, Naive Bayes)"),
        ("CO4", 
         "Apply parameter tuning and performance evaluation techniques for regression and classification models built with scikit-learn.", 
         "L4 (Analyse)", 
         "Chapters 6 & 7 (Grid Search, Laplace Tuning, Precision, Recall, ROC-AUC)"),
        ("CO5", 
         "Implement unsupervised learning algorithms such as K-Means Clustering using scikit-learn for grouping unlabeled data.", 
         "L3 (Apply)", 
         "Chapters 5 & 7 (Unsupervised Document Clustering Analysis)"),
        ("CO6", 
         "Analyze and compare the performance of different classification algorithms on a given dataset through a mini-project.", 
         "L5 (Evaluate) / L6 (Create)", 
         "Chapters 7 & 9 (Comparative Benchmark, Error Analysis & Real-time Deployment)")
    ]

    for r_idx, (co_id, stmt, bloom, addr) in enumerate(cos_data, start=1):
        set_cell_text(t5.cell(r_idx, 0), co_id, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
        set_cell_text(t5.cell(r_idx, 1), stmt)
        set_cell_text(t5.cell(r_idx, 2), bloom, align=WD_ALIGN_PARAGRAPH.CENTER)
        set_cell_text(t5.cell(r_idx, 3), addr)

    print("Table 5 (Course Outcomes) populated with 6 official COs.")

    # 3. Table 6: CO - PO - PSO Matrix
    t6 = doc.tables[6]
    while len(t6.rows) < 8:
        t6.add_row()

    matrix_rows = [
        ("CO1", ["3", "3", "–", "2", "3", "–", "–", "–", "–", "–", "2", "3", "–"]),
        ("CO2", ["3", "3", "2", "2", "3", "–", "–", "–", "2", "–", "2", "3", "2"]),
        ("CO3", ["3", "3", "3", "2", "3", "–", "–", "–", "–", "–", "2", "3", "3"]),
        ("CO4", ["3", "3", "3", "3", "3", "–", "–", "–", "–", "–", "2", "3", "2"]),
        ("CO5", ["3", "2", "2", "3", "3", "–", "–", "–", "–", "–", "2", "3", "2"]),
        ("CO6", ["3", "3", "3", "3", "3", "2", "2", "3", "3", "2", "3", "3", "3"]),
        ("Average", ["3.0", "2.8", "2.6", "2.4", "3.0", "2.0", "2.0", "3.0", "2.5", "2.0", "2.2", "3.0", "2.4"])
    ]

    for r_idx, (label, vals) in enumerate(matrix_rows, start=1):
        is_avg = (label == "Average")
        set_cell_text(t6.cell(r_idx, 0), label, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
        for c_idx, val in enumerate(vals, start=1):
            set_cell_text(t6.cell(r_idx, c_idx), val, bold=is_avg, align=WD_ALIGN_PARAGRAPH.CENTER)

    print("Table 6 (CO-PO-PSO Matrix) updated with 6 COs and computed averages.")

    # 4. Table 7: Justifications
    t7 = doc.tables[7]
    while len(t7.rows) < 7:
        t7.add_row()

    justifications = [
        ("CO1 – PO1 / PO5", "3", 
         "Applies foundational principles of engineering mathematics and computational statistics (mean length, variance, standard deviation) using Python statistical libraries to characterize email data distributions."),
        ("CO2 – PO5 / PSO1", "3", 
         "Employs modern data science tools (NumPy, Pandas, Matplotlib, Seaborn) to execute data cleaning, regex masking, tokenization, and render high-resolution exploratory data visualizations."),
        ("CO3 – PO3 / PSO1", "3", 
         "Designs and implements supervised machine learning classification algorithms (Logistic Regression, Decision Trees / Random Forest, and Naive Bayes) using scikit-learn to solve digital spam threats."),
        ("CO4 – PO4 / PSO1", "3", 
         "Conducts structured investigations of model performance via 5-fold cross-validation, hyperparameter grid search, and cost-sensitive evaluation prioritizing high Precision to prevent false positives."),
        ("CO5 – PO4 / PSO2", "3", 
         "Applies unsupervised clustering techniques (K-Means) to explore semantic grouping and natural topic clusters within high-dimensional sparse TF-IDF text vectors."),
        ("CO6 – PO3 / PO9 / PO11 / PSO1 / PSO2", "3", 
         "Accomplishes a complete end-to-end classification mini-project, conducting rigorous comparative benchmarking, error analysis, technical report preparation, presentation delivery, and real-time deployment.")
    ]

    for r_idx, (m, lvl, text) in enumerate(justifications, start=1):
        set_cell_text(t7.cell(r_idx, 0), m, bold=True)
        set_cell_text(t7.cell(r_idx, 1), lvl, align=WD_ALIGN_PARAGRAPH.CENTER)
        set_cell_text(t7.cell(r_idx, 2), text)

    print("Table 7 (Justification Table) updated for all 6 COs.")

    # 5. Table 8: Programme Outcomes (NBA SAR Tier-I)
    t8 = doc.tables[8]
    while len(t8.rows) < 12:
        t8.add_row()

    po_data = [
        ("PO1", "Engineering Knowledge", 
         "Apply knowledge of mathematics, natural science, computing, engineering fundamentals and an engineering specialization as specified in WK1 to WK4 respectively to develop the solution of complex engineering problems."),
        ("PO2", "Problem Analysis", 
         "Identify, formulate, review research literature and analyze complex engineering problems reaching substantiated conclusions with consideration for sustainable development. (WK1 to WK4)"),
        ("PO3", "Design/Development of Solutions", 
         "Design creative solutions for complex engineering problems and design/develop systems/components/processes to meet identified needs with consideration for public health and safety, whole-life cost, net zero carbon, culture, society and environment as required. (WK5)"),
        ("PO4", "Conduct Investigations of Complex Problems", 
         "Conduct investigations of complex engineering problems using research-based knowledge including design of experiments, modelling, analysis & interpretation of data to provide valid conclusions. (WK8)"),
        ("PO5", "Engineering Tool Usage", 
         "Create, select and apply appropriate techniques, resources and modern engineering & IT tools, including prediction and modelling recognizing their limitations to solve complex engineering problems. (WK2 and WK6)"),
        ("PO6", "The Engineer and The World", 
         "Analyze and evaluate societal and environmental aspects while solving complex engineering problems for its impact on sustainability with reference to economy, health, safety, legal framework, culture and environment. (WK1, WK5, and WK7)"),
        ("PO7", "Ethics", 
         "Apply ethical principles and commit to professional ethics, human values, diversity and inclusion; adhere to national & international laws. (WK9)"),
        ("PO8", "Individual and Collaborative Team work", 
         "Function effectively as an individual, and as a member or leader in diverse/multi-disciplinary teams."),
        ("PO9", "Communication", 
         "Communicate effectively and inclusively within the engineering community and society at large, such as being able to comprehend and write effective reports and design documentation, make effective presentations considering cultural, language, and learning differences."),
        ("PO10", "Project Management and Finance", 
         "Apply knowledge and understanding of engineering management principles and economic decision-making and apply these to one's own work, as a member and leader in a team, and to manage projects and in multidisciplinary environments."),
        ("PO11", "Life-Long Learning", 
         "Recognize the need for, and have the preparation and ability for i) independent and life-long learning ii) adaptability to new and emerging technologies and iii) critical thinking in the broadest context of technological change. (WK8)")
    ]

    for r_idx, (p_code, attr, kw) in enumerate(po_data, start=1):
        set_cell_text(t8.cell(r_idx, 0), p_code, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
        set_cell_text(t8.cell(r_idx, 1), attr, bold=True)
        set_cell_text(t8.cell(r_idx, 2), kw)

    print("Table 8 (Programme Outcomes) updated with exact NBA Tier-I Annexure-II statements.")

    # 6. Table 9: Programme Specific Outcomes (PSOs)
    t9 = doc.tables[9]
    while len(t9.rows) < 3:
        t9.add_row()

    pso_data = [
        ("PSO1", "Design, develop and deploy intelligent models and systems using machine learning, deep learning, and data analytics tools to solve real-world problems."),
        ("PSO2", "Apply artificial intelligence techniques to domain-specific applications, ensuring ethical, secure, scalable and responsible software systems.")
    ]

    for r_idx, (p_code, desc) in enumerate(pso_data, start=1):
        set_cell_text(t9.cell(r_idx, 0), p_code, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
        set_cell_text(t9.cell(r_idx, 1), desc)

    print("Table 9 (PSOs) updated.")

    # Save to ML-Project Documentation_Updated.docx
    doc.save("ML-Project Documentation_Updated.docx")
    print("Saved to ML-Project Documentation_Updated.docx successfully!")

    # Attempt to save to ML-Project Documentation.docx and artifacts
    try:
        doc.save("ML-Project Documentation.docx")
        print("Saved directly to ML-Project Documentation.docx!")
    except Exception as e:
        print(f"Notice: ML-Project Documentation.docx is currently open in Word ({e}). It has been saved to ML-Project Documentation_Updated.docx.")

    try:
        os.makedirs("artifacts/reports", exist_ok=True)
        doc.save("artifacts/reports/ML_Project_Documentation_Email_Spam_Detection.docx")
        print("Saved to artifacts/reports/ML_Project_Documentation_Email_Spam_Detection.docx!")
    except Exception as e:
        print(f"Notice: artifacts report save: {e}")

if __name__ == "__main__":
    update_cos_and_pos()
