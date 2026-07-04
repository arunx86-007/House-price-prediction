# 🏠 House Price Prediction using Machine Learning

## 📖 Overview

This project predicts house prices using Machine Learning based on property features such as location, area, number of bedrooms, bathrooms, balconies, furnishing status, and other housing attributes. The project follows a complete end-to-end machine learning workflow, from data preprocessing and model evaluation to deployment using Streamlit.

---

## 🎯 Problem Statement

The objective of this project is to build an accurate regression model capable of estimating house prices based on various property characteristics, helping users make informed real estate decisions.

---

## 📊 Dataset

The dataset contains residential property information collected from multiple cities across India.

**Target Variable**

- Amount (in rupees)

**Features**

- Location
- Area
- Bedrooms
- Bathrooms
- Balconies
- Furnishing Status
- Parking
- Property Type
- Floor Details
- Additional Property Features

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Joblib
- Streamlit

---

## ⚙️ Workflow

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing
- Train-Test Split
- Model Building
- Model Comparison
- Log Transformation Analysis
- Hyperparameter Tuning
- Model Deployment

---

## 🔍 Data Preprocessing

- Missing value imputation
- One-Hot Encoding
- Feature Scaling
- Pipeline and ColumnTransformer implementation
- Train-Test split to prevent data leakage

---

## 🤖 Models Evaluated

- Linear Regression
- Decision Tree Regressor
- K-Nearest Neighbors Regressor
- Random Forest Regressor
- Extra Trees Regressor
- Support Vector Regressor (SVR)
- XGBoost Regressor

---

## 📈 Model Comparison (Without Log Transformation)

| Model | R² | MAE | RMSE |
|------|----:|----:|-----:|
| **XGBoost** | **0.8020** | 2,324,250 | 4,054,813 |
| Extra Trees | 0.7956 | 2,290,998 | 4,119,780 |
| Random Forest | 0.7946 | 2,321,137 | 4,129,764 |
| Linear Regression | 0.6882 | 3,221,140 | 5,088,780 |
| KNN | 0.6654 | 2,972,938 | 5,271,231 |
| Decision Tree | 0.6104 | 3,085,892 | 5,687,929 |
| SVR | -0.1189 | 5,475,488 | 9,639,712 |

---

## 🔄 Log Transformation Analysis

To reduce the skewness of the target variable, models were trained with and without log transformation. Although log transformation improved the performance of some models, the original target values produced the best overall results with XGBoost.

---

## 🚀 Hyperparameter Tuning

RandomizedSearchCV with 5-fold Cross Validation was used to optimize the XGBoost model.

### Performance Improvement

| Metric | Before | After |
|---------|-------:|------:|
| **R² Score** | **0.8020** | **0.8046** |
| **MAE** | 2,324,250 | **2,307,286** |
| **RMSE** | 4,054,813 | **4,027,876** |

---

## 🏆 Final Model

**Algorithm:** XGBoost Regressor

| Metric | Value |
|---------|-------:|
| **R² Score** | **0.8046** |
| **MAE** | **2,307,286** |
| **RMSE** | **4,027,876** |

The tuned XGBoost model achieved the best predictive performance and was selected for deployment.

---

## 💻 Streamlit Application

The trained model is deployed using Streamlit, allowing users to enter property details and instantly receive a predicted house price.

---

## 📂 Project Structure

```
House-Price-Prediction/
│── data/
│── notebooks/
│── models/
│── app.py
│── requirements.txt
│── README.md
```

---

## 🚀 Installation

```bash
git clone https://github.com/your-username/House-Price-Prediction.git
cd House-Price-Prediction
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Future Improvements

- Deploy on Streamlit Community Cloud
- Add SHAP for model explainability
- Experiment with LightGBM and CatBoost
- Improve feature engineering

---

## 👨‍💻 Author

**Arun Singh**