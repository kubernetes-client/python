# Copyright 2018 The Kubernetes Authors.
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

import json


def api_call(api_client=None,path=None,method="GET"):
    local_var_params = locals()

    all_params = [
    ]

    all_params.extend(
        [
            'async_req',
            '_return_http_data_only',
            '_preload_content',
            '_request_timeout'
        ]
    )

    collection_formats = {}

    path_params = {}

    query_params = []

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = None
    # HTTP header `Accept`
    header_params['Accept'] = api_client.select_header_accept(
        ['application/json'])  # noqa: E501
    
    # Authentication setting
    auth_settings = ['BearerToken']

    return api_client.call_api(
        path, method,
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='str',  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get('async_req'),
        _return_http_data_only=True,  # noqa: E501
        _preload_content=local_var_params.get('_preload_content', True),
        _request_timeout=local_var_params.get('_request_timeout'),
        collection_formats=collection_formats
        )

 


def pods(api_client=None,all_namespaces=False,namespace=None,pod_name=None):
    """
    Queries the CPU and Memory Consumption of Kubernetes Pods. Python form of 
    kubernetes top pods command.

    Input:
    api_client: an ApiClient object, initialized with the client args.
    all_namespaces: bool. Should be set to return pod metrics from all 
        namespaces. Should not be set if either namespace or pod_name is 
        provided. 
    namespace: string. Namespace from which the pod metrics should be 
        retrieved. If not provided default namespace is set
    pod_name: string. Name of the pod to query the metrics. If not provided
        all pod metrics from the provided namespace is retrieved

    Returns:
        The list containing the node metrics if node_name is not provided.
        If node_name is provided, a json object containing the metrics of
        the node. 

    Raises:
        Raises Exception when the provided node does not exist. 
    """

    if all_namespaces and pod_name is not None:
        raise Exception("Error: all_namespaces and pod_name should not provided together")
    if all_namespaces and namespace is not None:
        raise Exception("Error: all_namespaces and namespace should not provided together")
    if all_namespaces:
        response = api_call(api_client=api_client,path=f"/apis/metrics.k8s.io/v1beta1/pods",method="GET")
        response = response.replace("\'", "\"")
        data = json.loads(response)
        items = data["items"]
        metrics = []
        for i in items:
            metrics.append({"namespace": i["metadata"]["namespace"],"pod_name":i["metadata"]["name"],"containers":i["containers"]})
        return metrics
    else:
        if namespace is None:
            namespace = "default"
        if pod_name is None:
            response = api_call(api_client=api_client,path=f"/apis/metrics.k8s.io/v1beta1/namespaces/{namespace}/pods",method="GET")
            response = response.replace("\'", "\"")
            data = json.loads(response)
            items = data["items"]
            metrics = []
            for i in items:
                metrics.append({"pod_name":i["metadata"]["name"],"containers":i["containers"]})
            return metrics
        else:
            try:
                response = api_call(api_client=api_client,path=f"/apis/metrics.k8s.io/v1beta1/namespaces/{namespace}/pods/{pod_name}",method="GET")
                response = response.replace("\'", "\"")
                data = json.loads(response)
                return {"pod_name": data["metadata"]["name"],"containers":data["containers"]}
            except Exception:
                raise Exception(f"Error: Pod {pod_name} not found in the {namespace} namespace")



def nodes(api_client=None,node_name=None):
    """
    Queries the CPU and Memory Consumption of Kubernetes Nodes. Python form of 
    kubernetes top nodes command.

    Input:
    api_client: an ApiClient object, initialized with the client args.
    node_name: string. Name of the node to query the metrics. If not provided
        will return the metrics of all the nodes

    Returns:
        The list containing the node metrics if node_name is not provided.
        If node_name is provided, a json object containing the metrics of
        the node. 

    Raises:
        Raises Exception when the provided node does not exist. 
    """

    if node_name is None:
        response = api_call(api_client=api_client,path="/apis/metrics.k8s.io/v1beta1/nodes",method="GET")
        response = response.replace("\'", "\"")
        data = json.loads(response)
        items = data["items"]
        metrics = []
        for i in items:
            metrics.append({"node_name":i["metadata"]["name"],"metrics":i["usage"]})
        return metrics
    else:
        try:
            response = api_call(api_client=api_client,path=f"/apis/metrics.k8s.io/v1beta1/nodes/{node_name}",method="GET")
            response = response.replace("\'", "\"")
            data = json.loads(response)
            return {
                "node_name":data["metadata"]["name"],
                "usage": data["usage"]
            }
        except Exception:
            raise Exception(f"Error {node_name} does not exist")
    

