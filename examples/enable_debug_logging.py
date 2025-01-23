# Copyright 2025 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# This example demonstrates how to enable debug logging in the Kubernetes
# Python client and how it can be used for troubleshooting requests/responses.

from kubernetes import client, config


def main():
    # Load kubeconfig from default location
    config.load_kube_config()

    # Enable debug logging
    configuration = client.Configuration()
    configuration.debug = True
    api_client = client.ApiClient(configuration=configuration)

    # Use AppsV1Api with debug logging enabled
    apps_v1 = client.AppsV1Api(api_client=api_client)

    # Example: Create a dummy deployment (adjust namespace as needed)
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name="debug-example"),
        spec=client.V1DeploymentSpec(
            replicas=1,
            selector={"matchLabels": {"app": "debug"}},
            template=client.V1PodTemplateSpec(
                metadata=client.V1ObjectMeta(labels={"app": "debug"}),
                spec=client.V1PodSpec(
                    containers=[
                        client.V1Container(
                            name="busybox",
                            image="busybox",
                            command=["sh", "-c", "echo Hello, Kubernetes! && sleep 3600"]
                        )
                    ]
                ),
            ),
        ),
    )

    # Create the deployment
    try:
        print("[INFO] Creating deployment...")
        apps_v1.create_namespaced_deployment(
            namespace="default", body=deployment
            )
    except client.exceptions.ApiException as e:
        print("[ERROR] Exception occurred:", e)


if __name__ == "__main__":
    main()
