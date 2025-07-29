
# Fraud Scoring Dashboard

This Streamlit dashboard allows you to interactively view and filter transaction fraud scores in real-time.

## Features

- Load transactions and apply a trained ML model
- Score each transaction with fraud probability
- Filter results by fraud score range
- Sort and inspect suspicious transactions

## How to Run

1. Install requirements:

```bash
pip install streamlit pandas numpy joblib
```

2. Start the app:

```bash
streamlit run dashboard/fraud_scoring_dashboard.py
```

3. Open browser to: http://localhost:8501

## Use Cases

- Fraud analyst investigation
- Model performance inspection
- Executive demo for fraud score thresholds

