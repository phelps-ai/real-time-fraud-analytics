
# Real-Time Fraud Detection with Kafka

This project demonstrates how to stream transactions into Kafka, score them in real-time using a machine learning model, and flag high-risk events for fraud alerts.

## Components

- `docker-compose.yml`: Spins up Kafka + Zookeeper
- `producer.py`: Simulates and streams transactions
- `consumer.py`: Scores transactions using ML model
- `model/`: Contains trained fraud model (from Project 1)
- `dashboard/`: Placeholder for real-time fraud alert dashboard

## How to Run

1. Start Kafka:
```
docker-compose up -d
```

2. Create Kafka topics:
```
docker exec -it <broker-container-id> kafka-topics --create --topic transactions --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
docker exec -it <broker-container-id> kafka-topics --create --topic fraud-alerts --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

3. Start the producer and consumer:
```
python producer/producer.py
python consumer/consumer.py
```

4. View fraud alerts in real-time.
