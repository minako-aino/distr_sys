from flask import Flask, request, jsonify
import requests
import uuid

app = Flask(__name__)

LOGGING_SERVICE_URL = "http://localhost:5001/log"  # Adjust the port accordingly
MESSAGES_SERVICE_URL = "http://localhost:5002/message"


@app.route('/facade', methods=['POST'])
def post_message():
    message = request.json.get('msg')
    unique_id = str(uuid.uuid4())
    response = requests.post(LOGGING_SERVICE_URL, json={'uuid': unique_id, 'msg': message})
    return jsonify({'uuid': unique_id, 'response': response.json()}), response.status_code


@app.route('/facade', methods=['GET'])
def get_messages():
    log_response = requests.get(LOGGING_SERVICE_URL)
    messages_response = requests.get(MESSAGES_SERVICE_URL)
    return jsonify({'logged_messages': " ".join(log_response.json()), 'static_message': messages_response.json()}), 200


if __name__ == '__main__':
    app.run(port=5000)
