from flask import Flask

app = Flask(__name__)


@app.route("/")
# core layer api to get all workspaces
def root():
    return "Hello World!"

@app.route("/core")
# core layer api to get all workspaces
def core():
    return "I am core!"


@app.route("/kernel")
# kernel layer api to get all workspaces
def kernel():
    return "I am kernel!"
