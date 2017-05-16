FROM nbgallery/jupyter-alpine:latest 

RUN pip install git+https://github.com/kubernetes-incubator/client-python.git

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["jupyter", "notebook", "--ip=0.0.0.0"]

