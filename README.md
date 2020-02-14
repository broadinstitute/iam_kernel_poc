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
```

Call core services with token, use:

```
curl -H "Authorization: Bearer ${TOKEN}" -v -i http://$INGRESS_HOST/core
```

Call kernel1 service from coreapp in k8s cluster:

```
kubectl exec $(kubectl get pod -l app=coreapp -n dev -o jsonpath={.items..metadata.name}) -c coreapp -n dev -- curl -i http://kernel1:8001/kernel
```


Call kernel2 service from coreapp in k8s cluster:

```
kubectl exec $(kubectl get pod -l app=coreapp -n dev -o jsonpath={.items..metadata.name}) -c coreapp -n dev -- curl -i http://kernel2:8002/kernel
```


