#!/usr/bin/python3
# -*- coding:utf-8 -*-

import json
import time

from kubernetes import client, config

config.load_kube_config()


def create_namespaced_cron_job(namespace='default', body=None):
    cronjob_json = body
    if body is None:
        print('body is required!')
        exit(0)
    name = body['metadata']['name']
    if judge_crontab_exists(namespace, name):
        print(f'{name} exists, please do not repeat!')
    else:
        v1 = client.BatchV1Api()
        ret = v1.create_namespaced_cron_job(namespace=namespace, body=cronjob_json, pretty=True,
                                            _preload_content=False, async_req=False)
        ret_dict = json.loads(ret.data)
        print(f'create succeed\n{json.dumps(ret_dict)}')


def delete_namespaced_cron_job(namespace='default', name=None):
    if name is None:
        print('name is required!')
        exit(0)
    if not judge_crontab_exists(namespace, name):
        print(f"{name} doesn't exists, please enter a new one!")
    else:
        v1 = client.BatchV1Api()
        ret = v1.delete_namespaced_cron_job(name=name, namespace=namespace, _preload_content=False, async_req=False)
        ret_dict = json.loads(ret.data)
        print(f'delete succeed\n{json.dumps(ret_dict)}')


def patch_namespaced_cron_job(namespace='default', body=None):
    cronjob_json = body
    if body is None:
        print('body is required!')
        exit(0)
    name = body['metadata']['name']
    if judge_crontab_exists(namespace, name):
        v1 = client.BatchV1Api()
        ret = v1.patch_namespaced_cron_job(name=name, namespace=namespace, body=cronjob_json,
                                           _preload_content=False, async_req=False)
        ret_dict = json.loads(ret.data)
        print(f'patch succeed\n{json.dumps(ret_dict)}')
    else:
        print(f"{name} doesn't exists, please enter a new one!")


def get_cronjob_list(namespace='default'):
    v1 = client.BatchV1Api()
    ret = v1.list_namespaced_cron_job(namespace=namespace, pretty=True, _preload_content=False)
    cron_job_list = json.loads(ret.data)
    print(f'cronjob number={len(cron_job_list["items"])}')
    return cron_job_list["items"]


def judge_crontab_exists(namespace, name):
    cron_job_list = get_cronjob_list(namespace)
    for cron_job in cron_job_list:
        if name == cron_job['metadata']['name']:
            return True
    return False


def get_cronjob_body(namespace, name, command):
    body = {
        "apiVersion": "batch/v1",
        "kind": "CronJob",
        "metadata": {
            "name": name,
            "namespace": namespace
        },
        "spec": {
            "schedule": "*/1 * * * *",
            "concurrencyPolicy": "Allow",
            "suspend": False,
            "jobTemplate": {
                "spec": {
                    "template": {
                        "spec": {
                            "containers": [
                                {
                                    "name": name,
                                    "image": "busybox:1.35",
                                    "command": command
                                }
                            ],
                            "restartPolicy": "Never"
                        }
                    }
                }
            },
            "successfulJobsHistoryLimit": 3,
            "failedJobsHistoryLimit": 1
        }
    }
    return body


if __name__ == '__main__':
    # get
    cronjob_list = get_cronjob_list()

    # delete
    delete_namespaced_cron_job('default', 'hostname')
    time.sleep(2)

    # create
    container_command = [
        "/bin/sh",
        "-c",
        "date; echo Hello from the Kubernetes cluster; hostname"
    ]
    hostname_json = get_cronjob_body('default', 'hostname', container_command)
    create_namespaced_cron_job('default', hostname_json)

    # update
    container_command[2] = "date; echo this is patch; hostname"
    hostname_json = get_cronjob_body('default', 'hostname', container_command)
    patch_namespaced_cron_job('default', hostname_json)
