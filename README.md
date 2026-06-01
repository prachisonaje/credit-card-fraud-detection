# Credit Card Fraud Detection using Machine Learning

## Overview

This project presents a comparative study of multiple Machine Learning algorithms for detecting fraudulent credit card transactions. The objective is to identify fraudulent activities accurately while minimizing false positives and false negatives.

Due to the highly imbalanced nature of credit card transaction datasets, the Synthetic Minority Oversampling Technique (SMOTE) is applied to improve model performance and enhance fraud detection capabilities.

## Features

- Data preprocessing and cleaning
- Class imbalance handling using SMOTE
- Fraud detection using multiple ML algorithms
- Comparative performance analysis
- ROC Curve visualization
- Confusion Matrix evaluation
- Accuracy, Precision, Recall, and F1-Score comparison
- Interactive web interface for dataset upload and prediction

## Algorithms Implemented

- Logistic Regression (LR)
- Decision Tree (DT)
- Random Forest (RF)
- XGBoost
- AdaBoost
- Local Outlier Factor (LOF)

## Tech Stack

### Programming Language
- Python

### Libraries
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost
- Imbalanced-Learn (SMOTE)

### Frontend
- Svelte

### Development Tools
- Google Colab
- Visual Studio Code

## Dataset

The project uses the Credit Card Fraud Detection Dataset containing:

- PCA transformed features (V1-V28)
- Time
- Amount
- Class

Target Variable:
- 0 → Legitimate Transaction
- 1 → Fraudulent Transaction

## Methodology

1. Data Collection
2. Data Preprocessing
3. Handling Missing Values
4. Feature Scaling
5. Train-Test Split (80:20)
6. Apply SMOTE to Balance Classes
7. Train Multiple ML Models
8. Evaluate Performance Metrics
9. Compare Results
10. Predict Fraudulent Transactions

## System Workflow

User Login
↓
Upload Transaction Dataset
↓
Data Preprocessing
↓
Model Prediction
↓
Fraud Analysis
↓
Performance Evaluation
↓
Result Generation

## Performance Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix

## Results

Among all the evaluated algorithms:

| Algorithm | Performance |
|------------|-------------|
| Logistic Regression | Moderate |
| Decision Tree | Good |
| Random Forest | Very Good |
| AdaBoost | Excellent |
| XGBoost | Best Performance |
| LOF | Anomaly Detection Analysis |

XGBoost achieved the highest fraud detection performance with excellent ROC-AUC and classification accuracy.

## Project Structure

├── dataset/
├── notebooks/
├── models/
├── screenshots/
├── app/
├── requirements.txt
├── README.md
└── main.py

## Future Enhancements

- Deep Learning based fraud detection
- Real-time transaction monitoring
- Streaming data processing
- Explainable AI (XAI)
- Cloud deployment
- API integration with banking systems

## Screenshots

- Home Page
  <img width="833" height="465" alt="image" src="https://github.com/user-attachments/assets/dbc17367-eae3-4ee0-9f6f-80f9584a0164" />

- Dashboard
  <img width="832" height="467" alt="image" src="https://github.com/user-attachments/assets/a8f08db3-a682-4ae6-acb8-0b5812be24b8" />

- Dataset Upload
  <img width="832" height="467" alt="image" src="https://github.com/user-attachments/assets/e9098030-d66d-4388-a0fb-9aa13daf7eb6" />

- Prediction Results
  <img width="835" height="469" alt="image" src="https://github.com/user-attachments/assets/cecee3db-2281-49f5-88b3-d531e300a4e6" />

- Achieved best ROC Curve with XGBoost 
  <img width="600" height="463" alt="image" src="https://github.com/user-attachments/assets/f5d9b846-aa3f-4892-ab3b-ba1aefa99f0b" />

- Confusion Matrix with XGBoost
  <img width="596" height="603" alt="image" src="https://github.com/user-attachments/assets/19727b7e-16c0-4362-a0e4-73a4247c4f7b" />


## Authors

- Prachi Sonaje
- Rifat Perween
- Nisha Kumari Singh

## License

This project is developed for academic and research purposes.
