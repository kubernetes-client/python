from kubernetes.client.rest import ApiException
from kubernetes import client, config
from kubernetes.client.api_client import ApiClient


class ConfigMapLock:
    def __init__(self, name, namespace, identity):
        """
        :param name: name of the lock
        :param namespace: namespace
        :param identity: A unique identifier that the candidate is using
        """
        self.api_instance = client.CoreV1Api()
        self.LeaderElectionRecordAnnotationKey = 'control-plane.alpha.kubernetes.io/leader'
        self.name = name
        self.namespace = namespace
        self.identity = identity

    # Get returns the election record from a ConfigMap Annotation
    def Get(self, name, namespace):
        """
        :param name: Name of the configmap object information to get
        :param namespace: Namespace in which the configmap object is to be searched
        :return: True, response if object found else False, exception
        """
        try:
            api_response = self.api_instance.read_namespaced_config_map(name, namespace)
            return True, api_response
        except ApiException as e:
            # print("Exception when calling CoreV1Api from ConfigMapLock.Get()->read_namespaced_config_map: %s\n" % e)
            return False, e

    def Create(self, name, namespace, electionRecord):
        """
        :param electionRecord: Annotation string
        :param name: Name of the configmap object to be created
        :param namespace: Namespace in which the configmap object is to be created
        :return: 'True, None' if object is created else 'False, error' if failed
        """
        body = client.V1ConfigMap(
            metadata={"name": name, "annotations": {self.LeaderElectionRecordAnnotationKey: str(electionRecord)}})  # V1ConfigMap | Name is a necessary metadata for a configmap object

        try:
            api_response = self.api_instance.create_namespaced_config_map(namespace, body, pretty=True)
            return True, api_response
        except ApiException as e:
            # print("Exception when calling CoreV1Api from ConfigMapLock.Create()->create_namespaced_config_map: %s\n" % e)
            return False, e

    def Update(self, name, namespace, updatedRecord):
        """
        :param name: name of the lock to be updated
        :param namespace: namespace the lock is in
        :param ElectionRecord: the updated record
        :return: True if update is succesful False if it fails
        """
        try:
            api_response = self.api_instance.replace_namespaced_config_map(name=name, namespace=namespace, body=updatedRecord)
            return True, api_response
        except ApiException as e:
            # print("Exception when calling CoreV1Api->replace_namespaced_config_map: %s\n" % e)
            return False, e
