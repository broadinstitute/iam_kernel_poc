from flask import Flask
import requests

app = Flask(__name__)

_KERNEL1_URL = 'http://kernel1:8001'

_KERNEL2_URL = 'http://kernel2:8002'

_KERNEL_PATH = "/kernel"


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


@app.route("/coreToKernel1")
# kernel layer api to get all workspaces
def core_to_kernel1():
    requests.get(_KERNEL1_URL + _KERNEL_PATH)
    return "Core to kernel1 "


@app.route("/coreToKernel2")
# kernel layer api to get all workspaces
def core_to_kernel2():
    requests.get(_KERNEL2_URL + _KERNEL_PATH)
    return "Core to kernel2 "
