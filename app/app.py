from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )
    return conn

@app.route('/')
def home():
    return jsonify({"message": "Docker Dev Stack is running!"})

@app.route('/health')
def health():
    try:
        conn = get_db()
        conn.close()
        return jsonify({"status": "healthy", "database": "connected"})
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)