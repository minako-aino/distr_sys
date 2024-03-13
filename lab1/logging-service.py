from flask import Flask, request, jsonify

app = Flask(__name__)

messages = {}


@app.route('/log', methods=['POST', 'GET'])
def log_message():
    if request.method == 'POST':
        data = request.json
        messages[data['uuid']] = data['msg']
        return jsonify({'status': 'Message logged'}), 200

    elif request.method == 'GET':
        return jsonify(list(messages.values())), 200


if __name__ == '__main__':
    app.run(port=5001)
