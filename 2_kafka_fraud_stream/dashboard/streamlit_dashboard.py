
import streamlit as st
from kafka import KafkaConsumer
import json

st.set_page_config(page_title="Fraud Alerts Dashboard", layout="wide")
st.title("🔍 Real-Time Fraud Alert Dashboard")

st.markdown("Streaming fraud alerts from Kafka topic: `fraud-alerts`")

consumer = KafkaConsumer(
    'fraud-alerts',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

placeholder = st.empty()

with placeholder.container():
    st.subheader("🚨 Live Fraud Alerts")
    log_box = st.empty()
    logs = []

    for msg in consumer:
        txn = msg.value
        alert_msg = (
            f"User: {txn['user_id']} | "
            f"Amount: ${txn['amount']} | "
            f"Country: {txn['country']} | "
            f"Device: {txn['device_type']} | "
            f"Fraud Score: {txn['fraud_score']:.2f}"
        )
        logs.insert(0, alert_msg)
        logs = logs[:10]  # Keep only last 10 alerts
        log_box.markdown("### Recent Alerts
" + "
".join([f"- {l}" for l in logs]))
