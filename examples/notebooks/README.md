Jupyter Notebooks for Kubernetes
================================

This is a set of Jupyter notebooks to learn the Kubernetes API in Python.

Launch the deployment and create the service.

```
kubectl create -f docker/jupyter.yml
```

Open your browser on the jupyter service and go through the notebooks.

If you are using minikube, you can run this command to see jupyter service in your browser:

```
minikube service jupyter
```

