
from kafka import KafkaProducer
import json
import time
import random
import uuid

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def generate_transaction():
    return {
        "transaction_id": str(uuid.uuid4()),
        "user_id": random.randint(1000, 1100),
        "amount": round(random.expovariate(1/100), 2),
        "country": random.choice(["US", "UK", "CN", "IN", "DE", "BR"]),
        "device_type": random.choice(["mobile", "desktop"])
    }

while True:
    txn = generate_transaction()
    producer.send("transactions", txn)
    print("Sent:", txn)
    time.sleep(1)
