from flask import Flask

app = Flask(__name__)


@app.route("/core", method=['GET'])
# core layer api to get all workspaces
def workspace():
    return "workspace found in core layer!"


@app.route("/kernel", method=['GET'])
# kernel layer api to get all workspaces
def workspace():
    return "I am kernel"
