import time

from kubernetes import config
from kubernetes.client import Configuration
from kubernetes.client.apis import core_v1_api
from kubernetes.client.rest import ApiException
from kubernetes.stream import stream

config.load_kube_config()
c = Configuration()
c.assert_hostname = False
Configuration.set_default(c)
api = core_v1_api.CoreV1Api()
name = 'busybox-test'

resp = None
try:
    resp = api.read_namespaced_pod(name=name,
                                   namespace='default')
except ApiException as e:
    if e.status != 404:
        print("Unknown error: %s" % e)
        exit(1)

if not resp:
    print("Pod %s does not exist. Creating it..." % name)
    pod_manifest = {
        'apiVersion': 'v1',
        'kind': 'Pod',
        'metadata': {
            'name': name
        },
        'spec': {
            'containers': [{
                'image': 'busybox',
                'name': 'sleep',
                "args": [
                    "/bin/sh",
                    "-c",
                    "while true;do date;sleep 5; done"
                ]
            }]
        }
    }
    resp = api.create_namespaced_pod(body=pod_manifest,
                                     namespace='default')
    while True:
        resp = api.read_namespaced_pod(name=name,
                                       namespace='default')
        if resp.status.phase != 'Pending':
            break
        time.sleep(1)
    print("Done.")


# calling exec and wait for response.
exec_command = [
    '/bin/sh',
    '-c',
    'echo This message goes to stderr >&2; echo This message goes to stdout']
resp = stream(api.connect_get_namespaced_pod_exec, name, 'default',
              command=exec_command,
              stderr=True, stdin=False,
              stdout=True, tty=False)
print("Response: " + resp)

# Calling exec interactively.
exec_command = ['/bin/sh']
resp = stream(api.connect_get_namespaced_pod_exec, name, 'default',
              command=exec_command,
              stderr=True, stdin=True,
              stdout=True, tty=False,
              _preload_content=False)
commands = [
    "echo test1",
    "echo \"This message goes to stderr\" >&2",
]
while resp.is_open():
    resp.update(timeout=1)
    if resp.peek_stdout():
        print("STDOUT: %s" % resp.read_stdout())
    if resp.peek_stderr():
        print("STDERR: %s" % resp.read_stderr())
    if commands:
        c = commands.pop(0)
        print("Running command... %s\n" % c)
        resp.write_stdin(c + "\n")
    else:
        break

resp.write_stdin("date\n")
sdate = resp.readline_stdout(timeout=3)
print("Server date command returns: %s" % sdate)
resp.write_stdin("whoami\n")
user = resp.readline_stdout(timeout=3)
print("Server user is: %s" % user)
resp.close()
