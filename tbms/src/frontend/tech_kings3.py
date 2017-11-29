from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def login():
    return render_template("login.html")


@app.route('/administration', methods=['POST', 'GET'])
def administration():
    return render_template("administration.html")


if __name__ == "__main__":
    app.run()
