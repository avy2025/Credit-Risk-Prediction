# Credit Risk Prediction 💳 📊

![Credit Risk Project Banner](banner.png)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🔍 Project Overview

This project implements an end-to-end **Credit Risk Prediction** system designed to help financial institutions minimize losses by identifying high-risk loan applicants. The solution addresses real-world challenges such as **class imbalance** and **business risk optimization**.

---

## 🎯 Problem Statement

Banks must balance two competing goals:
1. **Minimize Credit Loss:** Avoid approving loans for high-risk customers who might default.
2. **Maximize Opportunity:** Avoid rejecting low-risk customers, ensuring the bank doesn't lose profitable business.

This project leverages Machine Learning to predict default risk based on a comprehensive set of financial and personal attributes.

---

## 📂 Dataset: German Credit Risk

The model is trained on the **UCI German Credit Risk Dataset**, a gold standard for credit scoring research.

- **Size:** 1,000 records
- **Features:** 20 (Duration, Credit Amount, Employment, Savings, etc.)
- **Target:** 
    - `0` → No Default
    - `1` → Default

---

## ⚙️ Tech Stack

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn" />
  <img src="https://img.shields.io/badge/Matplotlib-ffffff?style=for-the-badge&logo=matplotlib&logoColor=black" alt="Matplotlib" />
  <img src="https://img.shields.io/badge/Seaborn-444444?style=for-the-badge&logo=seaborn&logoColor=white" alt="Seaborn" />
</p>

---

## 🧠 Machine Learning Approach

### Models Explored
- **Logistic Regression:** Used as a baseline for high explainability and business transparency.
- **Random Forest Classifier:** Used to capture non-linear relationships and complex feature interactions.

### Key Engineering Steps
- **Preprocessing:** One-Hot Encoding for categorical features & Standard Scaling.
- **Evaluation:** Focused on **Recall** (Defaulter Detection) and **Precision** tradeoff.
- **Optimization:** **Threshold Tuning** to align model predictions with business cost-benefit analysis.

---

## 📈 Key Results

| Metric (Default Class) | Baseline (Threshold 0.5) | Optimized (Tuned Threshold) |
| :--- | :---: | :---: |
| **Recall** | ~0.50 | **0.77** 🚀 |
| **Precision** | ~0.67 | 0.59 |
| **ROC-AUC** | ~0.80 | ~0.80 |

> [!IMPORTANT]
> **Threshold tuning** was the single most impactful step, increasing defaulter detection (Recall) by **54%**, which is critical for minimizing financial losses in banking.

---

## 💡 Business Insights

- ⏳ **Duration Matters:** Longer loan terms significantly correlate with higher default probability.
- 📜 **Credit History:** Past behavior remains the strongest predictor of future risk.
- 💰 **Financial Stability:** High savings accounts and stable long-term employment are the strongest indicators of creditworthiness.

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python installed. Clone the repository and navigate to the project directory.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Analysis
You can view the full analysis and model training in the Jupyter Notebook:
```bash
jupyter notebook Credit_Risk_Prediction.ipynb
```

---

## 🛠️ Future Roadmap

- [ ] **SHAP Explainability:** Detailed local and global feature impact analysis.
- [ ] **Hyperparameter Ops:** Automated tuning using Optuna or GridSearchCV.
- [ ] **Deployment:** Create a real-time prediction API using **Streamlit** or **FastAPI**.
- [ ] **Drift Detection:** Implement monitoring for feature and concept drift.

---

## 👤 Author

**Ranjan Thakur**
- [GitHub](https://github.com/Ranjan-Thakur) *(Adjust link if needed)*
- [LinkedIn](https://linkedin.com/in/ranjan-thakur) *(Adjust link if needed)*

---
*Developed with ❤️ for Fintech and Data Science.*