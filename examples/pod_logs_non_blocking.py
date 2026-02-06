"""
Non-blocking pod log streaming example.

Demonstrates how to stream Kubernetes pod logs without blocking indefinitely
by using socket timeouts and graceful shutdown.
"""

import threading
import time
import socket
from kubernetes import client, config
from urllib3.exceptions import ReadTimeoutError

stop_event = threading.Event()


def stream_logs():
    config.load_kube_config()
    v1 = client.CoreV1Api()

    resp = v1.read_namespaced_pod_log(
        name="log-demo",
        namespace="default",
        follow=True,
        _preload_content=False
    )

    # 👇 make socket non-blocking with timeout
    resp._fp.fp.raw._sock.settimeout(1)

    try:
        while not stop_event.is_set():
            try:
                data = resp.read(1024)
                if data:
                    print(data.decode(), end="")
            except (socket.timeout, ReadTimeoutError):
                continue
    finally:
        resp.close()
        print("\nLog streaming stopped cleanly.")


t = threading.Thread(target=stream_logs)
t.start()

try:
    time.sleep(15)
finally:
    stop_event.set()
    t.join()
