from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "<p>Hello from task1!</p>"


@app.route("/dog")
def main_dog():
    return "<p>Hello from dog1!</p>"

