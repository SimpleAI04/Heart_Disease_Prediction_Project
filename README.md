# ❤️ Heart Disease Prediction Project

This project aims to predict the likelihood of heart disease in patients based on clinical data using a **Random Forest Classifier**. The model is deployed via a simple web app built with **Streamlit**.

---

## 🩺 Overview

- 🔍 Input: Patient health attributes (e.g., age, cholesterol, blood pressure)
- 🎯 Output: Binary prediction (Heart Disease: Yes/No)
- 🧠 Model: Random Forest (pre-trained and saved as `.pkl`)
- 🖥️ Demo: Streamlit app for user interaction and prediction

---

## 📁 Project Structure
```
Heart_Disease_Prediction_Project/
│
├── Dataset/
│ └── heart(1).csv # Dataset with clinical records
│
├── Demo/
│ ├── app.py # Streamlit web app
│ └── model_randomforest.pkl # Trained ML model
│
├── Models/
│ ├── Benh_tim.ipynb # Exploratory analysis & experiments
│ └── BuildRandomForestClassifier.ipynb # Model training & saving
│
└── README.md # Project documentation
```
---

## ▶️ How to Run

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
2. **Run the app**
    ```bash
    streamlit run Demo/app.py
    
## 🧪 Dataset
Source: UCI Heart Disease Dataset

Contains features like:
Age, Sex, Chest Pain Type
Cholesterol, Resting BP, Max HR
Fasting blood sugar, ECG, Exercise-induced angina, etc.

## 🔍 Model
- Type: RandomForestClassifier from scikit-learn
- Preprocessed using standard scaling and label encoding
- Model saved as: Demo/model_randomforest.pkl

