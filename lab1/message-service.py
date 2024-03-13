from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/message', methods=['GET'])
def static_message():
    return jsonify('Not implemented yet'), 200


if __name__ == '__main__':
    app.run(port=5002)
