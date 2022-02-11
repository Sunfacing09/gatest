from re import L
from flask import Flask

app = Flask(__name__)

@app.route('/',methods=["GET"])
def index():
    return "Hello World"


@app.route('/promotion', methods=['GET', 'POST'])
def promotion():
    return "Promotion Page"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)