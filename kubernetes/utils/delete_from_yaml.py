import re
from os import path

import yaml

from kubernetes import client


def delete_from_yaml(
        k8s_client,
        yaml_file,
        verbose=False,
        namespace="default",
        **kwargs):
        '''
        Input:
        yaml_file: string. Contains the path to yaml file.
        k8s_client: an ApiClient object, initialized with the client args.
        verbose: If True, print confirmation from the create action.
            Default is False.
        namespace: string. Contains the namespace to create all
            resources inside. The namespace must preexist otherwise
            the resource creation will fail. If the API object in
            the yaml file already contains a namespace definition
            this parameter has no effect.
        Available parameters for creating <kind>:
        :param async_req bool
        :param bool include_uninitialized: If true, partially initialized
            resources are included in the response.
        :param str pretty: If 'true', then the output is pretty printed.
        :param str dry_run: When present, indicates that modifications
            should not be persisted. An invalid or unrecognized dryRun
            directive will result in an error response and no further
            processing of the request.
            Valid values are: - All: all dry run stages will be processed
        Raises:
            FailToCreateError which holds list of `client.rest.ApiException`
            instances for each object that failed to delete.
        '''
        # open yml file
        with open(path.abspath(yaml_file)) as f:
            #load all yml content
            yml_document_all = yaml.safe_load_all(f)
        
            failures=[]
            for yml_document in yml_document_all:
                try:
                    # call delete from dict function
                    delete_from_dict(k8s_client,yml_document,verbose,
                                 namespace=namespace,
                                 **kwargs)    
                except FailToCreateError as failure:
                    # if error is returned add to failures list
                    failures.extend(failure.api_exceptions)
            if failures:
                #display the error 
                raise FailToCreateError(failures)

def delete_from_dict(k8s_client,yml_document, verbose,namespace="default",**kwargs):
    """
    Perform an action from a dictionary containing valid kubernetes
    API object (i.e. List, Service, etc).
    Input:
    k8s_client: an ApiClient object, initialized with the client args.
    data: a dictionary holding valid kubernetes objects
    verbose: If True, print confirmation from the create action.
        Default is False.
    namespace: string. Contains the namespace to create all
        resources inside. The namespace must preexist otherwise
        the resource creation will fail. If the API object in
        the yaml file already contains a namespace definition
        this parameter has no effect.
    Raises:
        FailToCreateError which holds list of `client.rest.ApiException`
        instances for each object that failed to delete.
    """
    api_exceptions = []
    try:
        # call function delete_from_yaml_single_item 
        delete_from_yaml_single_item(
            k8s_client, yml_document, verbose, namespace=namespace, **kwargs
        )
    except client.rest.ApiException as api_exception:
        api_exceptions.append(api_exception)

    if api_exceptions:
        raise FailToCreateError(api_exceptions)


def delete_from_yaml_single_item(k8s_client, yml_document, verbose=False, **kwargs):
    # get group and version from apiVersion
    group,_,version = yml_document["apiVersion"].partition("/")
    if version == "":
        version = group
        group = "core"
    # Take care for the case e.g. api_type is "apiextensions.k8s.io"
    group = "".join(group.rsplit(".k8s.io", 1))
    # convert group name from DNS subdomain format to
    # python class name convention
    group = "".join(word.capitalize() for word in group.split('.'))
    group = "".join(word.capitalize() for word in group.split('.'))
    func = "{0}{1}Api".format(group, version.capitalize())
    k8s_api = getattr(client, func)(k8s_client)
    kind = yml_document["kind"]
    kind = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', kind)
    kind = re.sub('([a-z0-9])([A-Z])', r'\1_\2', kind).lower()

    if getattr(k8s_api,"delete_namespaced_{}".format(kind)):
        # load namespace if provided in yml file
        if "namespace" in yml_document["metadata"]:
            namespace = yml_document["metadata"]["namespace"]
            kwargs["namespace"] = namespace
        # take name input of kubernetes object
        name = yml_document["metadata"]["name"]
        #call function to delete from namespace
        res = getattr(k8s_api,"delete_namespaced_{}".format(kind))(
         name=name,body=client.V1DeleteOptions(propagation_policy="Foreground", grace_period_seconds=5),**kwargs)

    else:
        # get name of object to delete
        name = yml_document["metadata"]["name"]
        kwargs.pop('namespace', None)
        res = getattr(k8s_api,"delete_{}".format(kind))(
         name=name,body=client.V1DeleteOptions(propagation_policy="Foreground", grace_period_seconds=5),**kwargs)
    if verbose:
        msg = "{0} deleted.".format(kind)
        if hasattr(res, 'status'):
            msg += " status='{0}'".format(str(res.status))
        print(msg)
                

class FailToCreateError(Exception):
    """
    An exception class for handling error if an error occurred when
    handling a yaml file.
    """

    def __init__(self, api_exceptions):
        self.api_exceptions = api_exceptions

    def __str__(self):
        msg = ""
        for api_exception in self.api_exceptions:
            msg += "Error from server ({0}): {1}".format(
                api_exception.reason, api_exception.body)
        return msg
        
