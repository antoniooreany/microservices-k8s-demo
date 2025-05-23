import flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({"message": "Hello from Backend!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)