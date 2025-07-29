
# Real-Time Fraud Alerts Dashboard (WebSocket + React Style)

This dashboard enables real-time monitoring of fraud alerts streamed from Kafka using a WebSocket connection between a Flask backend and a simple HTML + JavaScript frontend.

---

## 📁 Project Structure

- `websocket_server.py`: Flask + Socket.IO backend that consumes Kafka `fraud-alerts` topic
- `fraud_dashboard.html`: Frontend UI that displays real-time fraud alerts
- `docker-compose.yml`: Kafka + Zookeeper setup
- `producer/`: Python script that streams fake transactions
- `consumer/`: Python script that scores transactions with ML model

---

## 🚀 How to Run (React + WebSocket Dashboard)

### Step 1: Start Kafka

Make sure Docker is installed, then run:

```bash
docker-compose up -d
```

Create Kafka topics if not already created:

```bash
docker exec -it <broker-container-id> kafka-topics --create --topic transactions --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
docker exec -it <broker-container-id> kafka-topics --create --topic fraud-alerts --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

### Step 2: Start Transaction Producer and Fraud Scorer

In two terminals:

```bash
python producer/producer.py
python consumer/consumer.py
```

### Step 3: Start WebSocket Server

Install dependencies:

```bash
pip install flask flask-socketio kafka-python eventlet
```

Then run:

```bash
python dashboard/websocket_server.py
```

This starts a Flask server on `http://localhost:5001`.

### Step 4: View Dashboard

Open the file `dashboard/fraud_dashboard.html` in your browser. It will connect to the WebSocket server and display real-time alerts streamed from Kafka.

> ✅ Note: Make sure you're running the backend and Kafka before loading the dashboard!

---

## 🔄 Customization Ideas

- Add sound or popup for high-risk alerts
- Group by user or device type
- Export alert logs to file or database
- Secure the WebSocket API for production use

---

This dashboard is perfect for demoing how your ML model scores and flags fraud events in real time using industry-ready architecture.

