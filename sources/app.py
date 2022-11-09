from flask import Flask, request
from calc import add2


app = Flask(__name__)


@app.route('/')
def main():
    return "this is python app"


@app.route('/calc')
def calculate():
    a = request.args.get('a')
    b = request.args.get('b')
    return f"{add2(a, b)}"


if __name__ == "__main__":
    app.run(debug=True)
