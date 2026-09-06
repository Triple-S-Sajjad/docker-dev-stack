from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def _require_env(name):
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value

def get_db():
    conn = psycopg2.connect(
        host=_require_env('DB_HOST'),
        database=_require_env('DB_NAME'),
        user=_require_env('DB_USER'),
        password=_require_env('DB_PASSWORD')
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