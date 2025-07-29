
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from kafka import KafkaConsumer
import json
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def consume_fraud_alerts():
    consumer = KafkaConsumer(
        'fraud-alerts',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='latest',
        enable_auto_commit=True,
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    for msg in consumer:
        socketio.emit('fraud_alert', msg.value)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    thread = threading.Thread(target=consume_fraud_alerts)
    thread.daemon = True
    thread.start()
    socketio.run(app, host='0.0.0.0', port=5001)
