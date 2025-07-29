
import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(page_title="Fraud Scoring Dashboard", layout="wide")
st.title("💳 Fraud Scoring Dashboard")

# Load data and model
@st.cache_data
def load_data():
    df = pd.read_csv("data/transactions.csv")
    return df

@st.cache_resource
def load_model():
    return joblib.load("model/rf_fraud_model.pkl")

data = load_data()
model = load_model()

# Feature engineering
data["amount_log"] = np.log1p(data["amount"])
data["is_foreign"] = (data["country"] != "US").astype(int)
data["device_score"] = data["device_type"].map({"mobile": 1, "desktop": 0})
features = ["amount_log", "is_foreign", "device_score"]

# Score predictions
data["fraud_score"] = model.predict_proba(data[features])[:, 1]

# Filters
st.sidebar.header("Filter Transactions")
min_score, max_score = st.sidebar.slider("Fraud Score Range", 0.0, 1.0, (0.0, 1.0), 0.01)
filtered = data[(data["fraud_score"] >= min_score) & (data["fraud_score"] <= max_score)]

# Display
st.metric("Total Transactions", len(data))
st.metric("Filtered Alerts", len(filtered))

st.dataframe(filtered[["user_id", "amount", "country", "device_type", "fraud_score"]].sort_values("fraud_score", ascending=False).reset_index(drop=True))
