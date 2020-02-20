from flask import Flask, request
import requests
import logging

app = Flask(__name__)

_COREAPP_URL = 'http://coreapp:8003'

_KERNEL1_URL = 'http://kernel1:8001'

_KERNEL2_URL = 'http://kernel2:8002'

_CORE_TO_KERNEL1_PATH = "/coreToKernel1"

_CORE_TO_KERNEL2_PATH = "/coreToKernel2"

_KERNEL_PATH = "/kernel"


@app.route("/")
# core layer api to get all workspaces
def root():
    return "Hello World!"


@app.route("/appToCoreToKernel1")
# App to core then to kernel1
def app_to_core_to_kernel1():
    user_jwt = request.headers.get("authorization")
    response = requests.get(
        _COREAPP_URL + _CORE_TO_KERNEL1_PATH,
        headers={'Authorization': user_jwt},
    )

    return "appToCoreToKernel1 " + str(response)


@app.route("/appToCoreToKernel2")
# App to core then to kernel1
def app_to_core_to_kernel2():
    user_jwt = request.headers.get("authorization")
    response = requests.get(
        _COREAPP_URL + _CORE_TO_KERNEL2_PATH,
        headers={'Authorization': user_jwt},
        )

    return "appToCoreToKernel2 " + str(response)


@app.route("/core")
# core layer api to get all workspaces
def core():
    return "I am core!"


@app.route("/kernel")
# kernel layer api to get all workspaces
def kernel():
    logging.warning("The caller is " + str(request.headers["X-Forwarded-Client-Cert"]))
    return "I am kernel!"


@app.route("/coreToKernel1")
# kernel layer api to get all workspaces
def core_to_kernel1():
    logging.warning("The caller is " + str(request.headers["X-Forwarded-Client-Cert"]))
    response = requests.get(_KERNEL1_URL + _KERNEL_PATH)

    return "coreToKernel1 " + str(response)


@app.route("/coreToKernel2")
# kernel layer api to get all workspaces
def core_to_kernel2():
    response = requests.get(_KERNEL2_URL + _KERNEL_PATH)
    return "coreToKernel2  " + str(response)

