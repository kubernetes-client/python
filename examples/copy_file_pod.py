# Copyright 2016 The Kubernetes Authors.
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

from kubernetes import client, config
from kubernetes.stream import stream
import tarfile
from tempfile import TemporaryFile
from kubernetes.client.rest import ApiException
from os import path


def copy_file_inside_pod(api_instance, pod_name, src_path, dest_path, namespace='default'):
    """
    This function copies a file inside the pod
    :param api_instance: coreV1Api()
    :param name: pod name
    :param ns: pod namespace
    :param source_file: Path of the file to be copied into pod
    :return: nothing
    """


    try:
        exec_command = ['tar', 'xvf', '-', '-C', '/']
        api_response = stream(api_instance.connect_get_namespaced_pod_exec, pod_name, namespace,
                              command=exec_command,
                              stderr=True, stdin=True,
                              stdout=True, tty=False,
                              _preload_content=False)

        with TemporaryFile() as tar_buffer:
            with tarfile.open(fileobj=tar_buffer, mode='w') as tar:
                tar.add(src_path, dest_path)

            tar_buffer.seek(0)
            commands = []
            commands.append(tar_buffer.read())

            while api_response.is_open():
                api_response.update(timeout=1)
                if api_response.peek_stdout():
                    print('STDOUT: {0}'.format(api_response.read_stdout()))
                if api_response.peek_stderr():
                    print('STDERR: {0}'.format(api_response.read_stderr()))
                if commands:
                    c = commands.pop(0)
                    api_response.write_stdin(c.decode())
                else:
                    break
            api_response.close()
    except ApiException as e:
        print('Exception when copying file to the pod: {0} \n'.format(e))


def copy_file_from_pod(api_instance, pod_name, src_path, dest_path, namespace="default"):
    """

    :param pod_name:
    :param src_path:
    :param dest_path:
    :param namespace:
    :return:
    """

    dir = path.dirname(src_path)
    bname = path.basename(src_path)
    exec_command = ['/bin/sh', '-c', 'cd {src}; tar cf - {base}'.format(src=dir, base=bname)]

    with TemporaryFile() as tar_buffer:
        resp = stream(api_instance.connect_get_namespaced_pod_exec, pod_name, namespace,
                      command=exec_command,
                      stderr=True, stdin=True,
                      stdout=True, tty=False,
                      _preload_content=False)

        while resp.is_open():
            resp.update(timeout=1)
            if resp.peek_stdout():
                out = resp.read_stdout()
                # print("STDOUT: %s" % len(out))
                tar_buffer.write(out.encode('utf-8'))
            if resp.peek_stderr():
                print('STDERR: {0}'.format(resp.read_stderr()))
        resp.close()

        tar_buffer.flush()
        tar_buffer.seek(0)

        with tarfile.open(fileobj=tar_buffer, mode='r:') as tar:
            subdir_and_files = [
                tarinfo for tarinfo in tar.getmembers()
            ]
            tar.extractall(path=dest_path, members=subdir_and_files)


def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()
    api = client.CoreV1Api()

    pod_name = 'nginx-0'    # Pod name to/from you want to copy file
    src_path = '/etc/hosts' # File/folder you want to copy
    dest_path = '/tmp'      # Destination path on which you want to copy the file/folder

    copy_file_from_pod(api_instance=api, pod_name=pod_name, src_path=src_path, dest_path=dest_path, namespace='default')
    copy_file_inside_pod(api_instance=api, pod_name=pod_name, src_path=src_path, dest_path=dest_path, namespace='default')

