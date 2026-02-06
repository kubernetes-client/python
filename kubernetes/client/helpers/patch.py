from kubernetes import client
from kubernetes.client.models import V1PodList

def apply_patch():
    """Monkeypatch ApiClient.deserialize safely."""
    if getattr(client.ApiClient, "_is_patched_for_terminating", False):
        return  # already patched

    original_deserialize = client.ApiClient.deserialize

    def _patched_deserialize(self, response, response_type):
        result = original_deserialize(self, response, response_type)
        if response_type == "V1PodList" and isinstance(result, V1PodList):
            for pod in result.items:
                if pod.metadata and pod.metadata.deletion_timestamp:
                    if pod.status and pod.status.phase == "Running":
                        pod.status.phase = "Terminating"
        return result

    client.ApiClient.deserialize = _patched_deserialize
    client.ApiClient._is_patched_for_terminating = True