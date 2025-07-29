# Fraud Detection Pipeline
This project simulates a basic fraud detection system using synthetic transaction data.

## Features Used
- Log-transformed transaction amount
- Foreign transaction indicator
- Device type score

## Model
- Random Forest Classifier

## Evaluation
- ROC AUC: 0.5018
- Confusion Matrix: [[1891, 52], [56, 1]]
- Classification Report:
  - 0: precision: 0.97, recall: 0.97, f1-score: 0.97, support: 1943.00
  - 1: precision: 0.02, recall: 0.02, f1-score: 0.02, support: 57.00
  - macro avg: precision: 0.50, recall: 0.50, f1-score: 0.50, support: 2000.00
  - weighted avg: precision: 0.94, recall: 0.95, f1-score: 0.95, support: 2000.00
