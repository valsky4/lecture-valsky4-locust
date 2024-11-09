import jwt as pyjwt
from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics
import time
import datetime

app = Flask(__name__)

# Initialize Prometheus Metrics
metrics = PrometheusMetrics(app)

# Secret key for JWT
SECRET_KEY = "your_secret_key"

def authenticate():
    """Check if the request has a valid JWT token."""
    token = request.headers.get("Authorization")
    if token:
        try:
            pyjwt.decode(token.split(" ")[-1], SECRET_KEY, algorithms=["HS256"])
            return True
        except pyjwt.ExpiredSignatureError:
            return False
        except pyjwt.InvalidTokenError:
            return False
    return False

@app.before_request
def require_authentication():
    """Require authentication for all endpoints except root, /login, and /metrics."""
    # NOTE: For demo purposes, /metrics is accessible without authentication.
    # In a production environment, ensure proper security for the /metrics endpoint.
    if request.path not in ["/", "/login", "/metrics"] and not authenticate():
        return jsonify(error="Authentication required: Please provide valid credentials"), 401

@app.route('/')
def index():
    return jsonify(message="Hello, World!"), 200

@app.route('/login', methods=['POST'])
def login():
    """Login endpoint to authenticate user and return a JWT token."""
    auth = request.json
    if auth and auth.get("username") == "admin" and auth.get("password") == "admin":
        token = pyjwt.encode(
            {
                'user': auth["username"],
                'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
            },
            SECRET_KEY,
            algorithm="HS256"
        )
        return jsonify(token=token), 200
    return jsonify(error="Invalid credentials"), 401

@app.route('/resource1')
def resource1():
    return jsonify(message="Resource 1"), 200

@app.route('/resource2')
def resource2():
    return jsonify(message="Resource 2"), 200

@app.route('/heavy-resource')
def heavy_resource():
    time.sleep(2)  # Simulate delay
    return jsonify(message="Heavy Resource"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
