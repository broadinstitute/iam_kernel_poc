# Demo Flask App

Used for https://broadworkbench.atlassian.net/browse/CA-660 

Build Docker image:

    docker build -f docker/Dockerfile -t iam_poc/flask_app .

Run the image:

    docker run --rm -p 5000:5000 iam_poc/flask_app

Access the app at: http://localhost:5000/

This will be reused for 2 different apps, i.e. a core app and a kernel app.

# Istio demo

Following along from https://istio.io/docs/tasks/traffic-management/ingress/ingress-control/

Trying to curl our coreapp:

Bring up our coreapp and our istio gateway. Cluster needs to be set up for automatic istio sidecar injection.
See [IAM POC notes](https://docs.google.com/document/d/1Ej51ummRutBXX65ZFnCUn2IBcvMeSgnZEC-V3RzQIFA/) about setitng up clusters.

```
kubectl apply -f config/core.yaml
kubectl apply -f config/istio_gateway.yaml
```

Grab the location of the gateway. Curl it asking it to redirect to our "coreapp.com".

```

export INGRESS_HOST=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')
export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].port}')


curl -i -HHost:coreapp.com http://$INGRESS_HOST:$INGRESS_PORT/core
```
