# Jupyter Notebooks for Kubernetes

This is a set of Jupyter notebooks to learn the Kubernetes API in Python.

Launch the deployment and create the service.

```
kubectl create -f docker/jupyter.yml
```

Open your browser on the jupyter service and go through the notebooks.

If you are using minikube:

```
# You can run this command to see jupyter service in your browser:

minikube service jupyter

# You can run this command to get the url in console
minikube service --url jupyter

```

Clean up your deployment.

```
kubectl delete -f docker/jupyter.yml
```
