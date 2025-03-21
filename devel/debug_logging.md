# Enabling Debug Logging in Kubernetes Python Client

This document describes how to enable debug logging, view logged information, and provides examples for creating, patching, and deleting Kubernetes resources.

## 1. Why Enable Debug Logging?

Debug logging is useful for troubleshooting as it shows details like HTTP request and response headers and bodies. These details can help identify issues during interactions with the Kubernetes API server.

---

## 2. Enabling Debug Logging

To enable debug logging in the Kubernetes Python client, follow these steps:

1. **Modify the Configuration Object:**
   Enable debug mode by setting the `debug` attribute of the `client.Configuration` object to `True`.

2. **Example Code to Enable Debug Logging:**
   Below is an example showing how to enable debug logging:
   ```python
   from kubernetes import client, config

   # Load kube config
   config.load_kube_config()

   # Enable debug logging
   c = client.Configuration()
   c.debug = True

   # Pass the updated configuration to the API client
   api_client = client.ApiClient(configuration=c)

   # Use the API client with debug logging enabled
   apps_v1 = client.AppsV1Api(api_client=api_client)
