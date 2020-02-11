from flask import Flask
import requests

app = Flask(__name__)

_KERNEL1_URL = 'localhost:5000'

_KERNEL2_URL = 'localhost:5000'

KERNEL_PATH = "/kernel"

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
def coreToKernel1():
    kernelResponse = requests.get(_KERNEL1_URL + KERNEL_PATH)
    return "Core to kernel1 " + kernelResponse;


@app.route("/coreToKernel2")
# kernel layer api to get all workspaces
def coreToKernel2():
    kernelResponse = requests.get(_KERNEL2_URL + KERNEL_PATH)
    return "Core to kernel2 " +  kernelResponse