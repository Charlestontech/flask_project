import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.errorhandler(Exception)
def handle_exception(e):
    # Generic error handling
    response = {
        'error': str(e),
        'message': 'An error occurred. Please try again later.'
    }
    return jsonify(response), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))