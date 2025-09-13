# app.py
from flask import Flask
from redis import Redis

app = Flask(__name__)
# 'redis' is the hostname of the Redis container in Docker Compose
redis = Redis(host='redis', port=6379, db=0, decode_responses=True)

@app.route('/')
def home():
    return "Welcome to the Flask + Redis web application!"

@app.route('/count')
def count():
    # Increment the 'visits' key in Redis
    redis.incr('visits')
    # Get the current count
    visits = redis.get('visits')
    return f"This page has been visited {visits} time(s)."

if __name__ == "__main__":
    # Run on all interfaces inside Docker
    app.run(host="0.0.0.0", port=5000, debug=True)

