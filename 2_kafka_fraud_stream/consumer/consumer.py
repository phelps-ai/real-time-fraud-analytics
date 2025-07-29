
from kafka import KafkaConsumer, KafkaProducer
import json
import joblib
import numpy as np

consumer = KafkaConsumer('transactions',
                         bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

model = joblib.load('model/rf_fraud_model.pkl')

def score(txn):
    amount_log = np.log1p(txn['amount'])
    is_foreign = 1 if txn['country'] != 'US' else 0
    device_score = 1 if txn['device_type'] == 'mobile' else 0
    X = np.array([[amount_log, is_foreign, device_score]])
    prob = model.predict_proba(X)[0, 1]
    return prob

for message in consumer:
    txn = message.value
    fraud_prob = score(txn)
    if fraud_prob > 0.8:
        txn['fraud_score'] = fraud_prob
        producer.send("fraud-alerts", txn)
        print("FRAUD ALERT:", txn)
