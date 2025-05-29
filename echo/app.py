import os

from flask import Flask
app = Flask(__name__)

@app.route("/ping")
def ping():
    return "pong"

@app.route("/secret-key")
def secret_key():
    secret = os.getenv("SECRET_KEY", "SECRET_KEY not found")
    return f"SECRET_KEY: {secret}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)