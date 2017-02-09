#!/bin/bash

# Copyright 2017 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -x

function clean_exit(){
    local error_code="$?"
    local spawned=$(jobs -p)
    if [ -n "$spawned" ]; then
        sudo kill $(jobs -p)
    fi
    return $error_code
}

trap "clean_exit" EXIT

# Switch off SE-Linux
setenforce 0

# Install docker if needed
path_to_executable=$(which docker)
if [ -x "$path_to_executable" ] ; then
    echo "Found Docker installation"
else
    curl -sSL https://get.docker.io | sudo bash
fi
docker --version

# Get the latest stable version of kubernetes
export K8S_VERSION=$(curl -sS https://storage.googleapis.com/kubernetes-release/release/stable.txt)
echo "K8S_VERSION : ${K8S_VERSION}"

echo "Starting docker service"
sudo systemctl enable docker.service
sudo systemctl start docker.service --ignore-dependencies
echo "Checking docker service"
sudo docker ps

echo "Download Kubernetes CLI"
wget -O kubectl "http://storage.googleapis.com/kubernetes-release/release/${K8S_VERSION}/bin/linux/amd64/kubectl"
sudo chmod +x kubectl
sudo mv kubectl /usr/local/bin/

echo "Download localkube from minikube project"
wget -O localkube "https://storage.googleapis.com/minikube/k8sReleases/v1.6.0-alpha.0/localkube-linux-amd64"
sudo chmod +x localkube
sudo mv localkube /usr/local/bin/

echo "Starting localkube"
sudo nohup localkube --logtostderr=true --enable-dns=false > localkube.log 2>&1 &

echo "Waiting for localkube to start..."
if ! timeout 120 sh -c "while ! curl -ks https://127.0.0.1:8443/ >/dev/null; do sleep 1; done"; then
    sudo cat localkube.log
    die $LINENO "localkube did not start"
fi

echo "Dump Kubernetes Objects..."
kubectl get componentstatuses
kubectl get configmaps
kubectl get daemonsets
kubectl get deployments
kubectl get events
kubectl get endpoints
kubectl get horizontalpodautoscalers
kubectl get ingress
kubectl get jobs
kubectl get limitranges
kubectl get nodes
kubectl get namespaces
kubectl get pods
kubectl get persistentvolumes
kubectl get persistentvolumeclaims
kubectl get quota
kubectl get resourcequotas
kubectl get replicasets
kubectl get replicationcontrollers
kubectl get secrets
kubectl get serviceaccounts
kubectl get services


echo "Running tests..."
set -x -e
# Yield execution to venv command
$*