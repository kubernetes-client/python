# Copyright 2026 The Kubernetes Authors.
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

from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import inspect
import json
from multiprocessing.pool import ApplyResult
import threading
import unittest

from pydantic import ValidationError

from kubernetes.client import (
    ApiClient,
    Configuration,
    CoreV1Api,
    CustomObjectsApi,
    V1ConfigMap,
    V1CustomResourceDefinitionVersion,
    V1CustomResourceValidation,
    V1ExecAction,
    V1HTTPGetAction,
    V1IPBlock,
    V1JSONSchemaProps,
    V1LifecycleHandler,
    V1ListMeta,
    V1NetworkPolicyIngressRule,
    V1NetworkPolicyPort,
    V1ObjectMeta,
    V1PodDisruptionBudgetSpec,
    V1PodList,
    V1Probe,
    V1RollingUpdateDaemonSet,
    V1RollingUpdateDeployment,
    V1RollingUpdateStatefulSetStrategy,
    V1ServicePort,
    V1StatusCause,
    V1TCPSocketAction,
)
from kubernetes.client.exceptions import NotFoundException
from kubernetes.utils import create_from_yaml
from kubernetes.watch import Watch


class _RecordingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.server.request_path = self.path
        self._respond()

    def do_PATCH(self):
        length = int(self.headers['Content-Length'])
        self.server.request_body = self.rfile.read(length)
        self.server.content_type = self.headers['Content-Type']
        self.server.request_path = self.path
        self._respond()

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        self.server.request_body = self.rfile.read(length)
        self.server.request_path = self.path
        self._respond()

    def do_DELETE(self):
        self.server.request_path = self.path
        self._respond()

    def _respond(self):
        response = self.server.response_body
        self.send_response(self.server.response_status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def log_message(self, format, *args):
        pass


class GeneratedModelTest(unittest.TestCase):
    def test_default_configuration_is_copied(self):
        previous_default = Configuration._default
        self.addCleanup(setattr, Configuration, '_default', previous_default)
        previous_api_client = ApiClient._default
        self.addCleanup(setattr, ApiClient, '_default', previous_api_client)
        ApiClient._default = None
        configured = Configuration(host='https://configured.example')
        configured.api_key['authorization'] = 'configured-token'
        configured.api_key_prefix['authorization'] = 'Bearer'
        Configuration.set_default(configured)
        configured.host = 'https://mutated.example'
        configured.api_key['authorization'] = 'mutated-token'
        configured.api_key_prefix['authorization'] = 'Mutated'

        first = CoreV1Api().api_client
        second = CoreV1Api().api_client

        self.assertEqual(
            'https://configured.example', first.configuration.host)
        self.assertEqual(
            'configured-token',
            first.configuration.api_key['authorization'],
        )
        self.assertEqual(
            'Bearer', first.configuration.api_key_prefix['authorization'])
        self.assertIsNot(first, second)
        self.assertIsNot(first.configuration, second.configuration)
        first.configuration.host = 'https://first.example'
        first.configuration.api_key['authorization'] = 'first-token'
        first.configuration.api_key_prefix['authorization'] = 'First'
        self.assertEqual(
            'https://configured.example', second.configuration.host)
        self.assertEqual(
            'configured-token',
            second.configuration.api_key['authorization'],
        )
        self.assertEqual(
            'Bearer', second.configuration.api_key_prefix['authorization'])

        Configuration.set_default(
            Configuration(host='https://replacement.example')
        )
        self.assertEqual(
            'https://replacement.example',
            CoreV1Api().api_client.configuration.host,
        )

    def test_model_constructor_uses_python_field_names(self):
        timestamp = datetime(2026, 6, 21, tzinfo=timezone.utc)

        metadata = V1ObjectMeta(creation_timestamp=timestamp)

        self.assertIn(
            'creation_timestamp', inspect.signature(V1ObjectMeta).parameters
        )
        self.assertNotIn(
            'creationTimestamp', inspect.signature(V1ObjectMeta).parameters
        )
        self.assertEqual(
            timestamp.isoformat().replace('+00:00', 'Z'),
            metadata.model_dump(mode='json', by_alias=True)[
                'creationTimestamp'
            ],
        )
        self.assertEqual(
            timestamp,
            V1ObjectMeta.model_validate({
                'creationTimestamp': timestamp.isoformat()
            }).creation_timestamp,
        )

    def test_model_fields_keep_public_names(self):
        exec_action = V1ExecAction(command=['true'])
        not_schema = V1JSONSchemaProps()
        validation = V1CustomResourceValidation()
        cases = [
            ('continue', V1ListMeta, {}, '_continue', 'token'),
            (
                'except',
                V1IPBlock,
                {'cidr': '10.0.0.0/8'},
                '_except',
                ['10.1.0.0/16'],
            ),
            ('exec', V1LifecycleHandler, {}, '_exec', exec_action),
            ('exec', V1Probe, {}, '_exec', exec_action),
            (
                'from',
                V1NetworkPolicyIngressRule,
                {},
                '_from',
                [],
            ),
            (
                'not',
                V1JSONSchemaProps,
                {},
                '_not',
                not_schema,
            ),
            (
                '$schema',
                V1JSONSchemaProps,
                {},
                'schema',
                'https://example.com/schema',
            ),
            ('field', V1StatusCause, {}, 'field', 'spec.value'),
            (
                'schema',
                V1CustomResourceDefinitionVersion,
                {'name': 'v1', 'served': True, 'storage': True},
                'schema',
                validation,
            ),
        ]

        for wire_name, model_type, required, attribute, expected in cases:
            with self.subTest(
                wire_name=wire_name, model_type=model_type.__name__
            ):
                model = model_type(**required, **{attribute: expected})
                self.assertEqual(expected, getattr(model, attribute))
                self.assertIn(attribute, inspect.signature(model_type).parameters)

                from_wire = model_type.model_validate({
                    **required, wire_name: expected
                })
                self.assertEqual(expected, getattr(from_wire, attribute))

                setattr(model, attribute, expected)
                self.assertEqual(expected, getattr(model, attribute))
                dumped = model.model_dump(by_alias=True, exclude_none=True)
                self.assertIn(wire_name, dumped)
                self.assertFalse(any(
                    name.startswith('var_') for name in dumped
                ))
                if attribute != wire_name:
                    self.assertNotIn(attribute, dumped)
                self.assertIn(
                    wire_name,
                    model_type.model_json_schema(
                        by_alias=True
                    )['properties'],
                )

    def test_model_field_alias_conflict_and_validation(self):
        with self.assertRaises(ValidationError):
            V1ListMeta.model_validate({
                'continue': 'wire',
                '_continue': 'legacy',
            })

        metadata = V1ListMeta(_continue='legacy')
        with self.assertRaises(ValidationError):
            metadata._continue = 1

    def test_nested_model_uses_legacy_attribute(self):
        pod_list = V1PodList.from_dict({
            'items': [],
            'metadata': {'continue': 'token'},
        })

        self.assertEqual('token', pod_list.metadata._continue)

    def test_to_dict_preserves_legacy_model_contract(self):
        pod_list = V1PodList(
            items=[], metadata=V1ListMeta(_continue='token'))
        timestamp = datetime(2026, 6, 21, tzinfo=timezone.utc)

        public = pod_list.to_dict()
        wire = pod_list.to_dict(serialize=True)
        public_metadata = V1ObjectMeta(
            creation_timestamp=timestamp).to_dict()
        wire_metadata = V1ObjectMeta(
            creation_timestamp=timestamp).to_dict(serialize=True)

        self.assertEqual('token', public['metadata']['_continue'])
        self.assertIn('remaining_item_count', public['metadata'])
        self.assertIsNone(public['metadata']['remaining_item_count'])
        self.assertEqual('token', wire['metadata']['continue'])
        self.assertIn('remainingItemCount', wire['metadata'])
        self.assertIsNone(wire['metadata']['remainingItemCount'])
        self.assertIn('creation_timestamp', public_metadata)
        self.assertNotIn('creationTimestamp', public_metadata)
        self.assertIn('creationTimestamp', wire_metadata)
        self.assertEqual({
            'items': [],
            'metadata': {'continue': 'token'},
        }, json.loads(pod_list.to_json()))

        class ExtendedListMeta(V1ListMeta):
            extra: str | None = None

        self.assertNotIn(
            'extra', ExtendedListMeta(_continue='token').to_dict())

    def test_api_client_serializes_models_for_requests(self):
        pod_list = V1PodList(
            items=[], metadata=V1ListMeta(_continue='token'))

        serialized = ApiClient().sanitize_for_serialization(pod_list)

        self.assertEqual({
            'items': [],
            'metadata': {'continue': 'token'},
        }, serialized)

    def test_int_or_string_fields_accept_both_representations(self):
        cases = [
            (V1RollingUpdateDaemonSet, {}, (
                ('max_surge', 'maxSurge'),
                ('max_unavailable', 'maxUnavailable'),
            )),
            (V1RollingUpdateDeployment, {}, (
                ('max_surge', 'maxSurge'),
                ('max_unavailable', 'maxUnavailable'),
            )),
            (V1RollingUpdateStatefulSetStrategy, {}, (
                ('max_unavailable', 'maxUnavailable'),
            )),
            (V1HTTPGetAction, {}, (('port', 'port'),)),
            (V1ServicePort, {'port': 80}, (
                ('target_port', 'targetPort'),
            )),
            (V1TCPSocketAction, {}, (('port', 'port'),)),
            (V1NetworkPolicyPort, {}, (('port', 'port'),)),
            (V1PodDisruptionBudgetSpec, {}, (
                ('max_unavailable', 'maxUnavailable'),
                ('min_available', 'minAvailable'),
            )),
        ]

        for model_type, required, fields in cases:
            for field, wire_name in fields:
                string_value = 'http' if 'port' in field else '25%'
                for value in (1, string_value):
                    with self.subTest(
                        model=model_type.__name__, field=field, value=value
                    ):
                        model = model_type(**required, **{field: value})
                        self.assertEqual(value, getattr(model, field))
                        self.assertEqual(
                            value,
                            model.model_dump(by_alias=True)[wire_name],
                        )
                for value in (True, 1.5, b'1'):
                    with self.subTest(
                        model=model_type.__name__, field=field, invalid=value
                    ):
                        with self.assertRaises(ValidationError):
                            model_type(**required, **{field: value})

    def test_json_schema_props_accepts_valid_crd_values(self):
        json_values = (False, 1, 1.5, 'value', [], {}, None)
        cases = [
            ('additional_items', 'additionalItems', (
                False, {'type': 'string'},
            )),
            ('additional_properties', 'additionalProperties', (
                True, {'type': 'integer'},
            )),
            ('default', 'default', json_values),
            ('dependencies', 'dependencies', (
                {'first': ['second']}, {'first': {'type': 'string'}},
            )),
            ('enum', 'enum', ([*json_values],)),
            ('example', 'example', json_values),
            ('items', 'items', (
                {'type': 'string'}, [{'type': 'string'}],
            )),
        ]

        for field, wire_name, values in cases:
            for value in values:
                with self.subTest(field=field, value=value):
                    schema = V1JSONSchemaProps(**{field: value})
                    self.assertEqual(value, getattr(schema, field))
                    self.assertEqual(
                        value, schema.model_dump(by_alias=True)[wire_name])

        for field in ('additional_items', 'additional_properties'):
            for value in ('false', 1):
                with self.subTest(field=field, invalid=value):
                    with self.assertRaises(ValidationError):
                        V1JSONSchemaProps(**{field: value})


class GeneratedApiTest(unittest.TestCase):
    def setUp(self):
        self.server = ThreadingHTTPServer(
            ('127.0.0.1', 0), _RecordingHandler)
        self.server.response_body = b'{}'
        self.server.response_status = 200
        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.start()
        self.api_client = ApiClient(Configuration(
            host=f'http://127.0.0.1:{self.server.server_port}',
            proxy='',
            no_proxy='',
        ))

    def tearDown(self):
        self.server.shutdown()
        self.thread.join()
        self.server.server_close()

    def test_continue_parameter_keeps_public_name(self):
        self.server.response_body = b'{"items": []}'

        namespaces = CoreV1Api(self.api_client).list_namespace(
            _continue='next-page')

        self.assertEqual([], namespaces.items)
        self.assertEqual(
            '/api/v1/namespaces?continue=next-page',
            self.server.request_path,
        )

    def test_deferred_api_validation_rejects_invalid_first_call(self):
        with self.assertRaises(ValidationError) as raised:
            CoreV1Api(self.api_client).list_namespace(limit='invalid')

        self.assertEqual(('limit',), raised.exception.errors()[0]['loc'])
        self.assertFalse(hasattr(self.server, 'request_path'))

    def test_delete_namespace_accepts_namespace_and_status_responses(self):
        responses = [
            {
                'apiVersion': 'v1',
                'kind': 'Namespace',
                'metadata': {'name': 'sample'},
                'status': {'phase': 'Terminating'},
            },
            {
                'apiVersion': 'v1',
                'kind': 'Status',
                'status': 'Success',
                'details': {'name': 'sample', 'kind': 'namespaces'},
            },
        ]

        for response in responses:
            with self.subTest(kind=response['kind']):
                self.server.response_body = json.dumps(response).encode()
                deleted = CoreV1Api(self.api_client).delete_namespace(
                    name='sample')

                self.assertEqual(response, deleted)
                self.assertEqual(
                    '/api/v1/namespaces/sample', self.server.request_path)

    def test_builtin_object_patch_defaults_to_strategic_merge_patch(self):
        body = {'data': {'key': 'value'}}

        CoreV1Api(self.api_client).patch_namespaced_config_map(
            name='sample', namespace='default', body=body)

        self.assertEqual(
            'application/strategic-merge-patch+json', self.server.content_type)
        self.assertEqual(body, json.loads(self.server.request_body))

    def test_builtin_model_patch_serializes_wire_aliases(self):
        body = V1ConfigMap(
            api_version='v1',
            kind='ConfigMap',
            metadata=V1ObjectMeta(name='sample', resource_version='7'),
            data={'key': 'value'},
        )

        CoreV1Api(self.api_client).patch_namespaced_config_map(
            name='sample', namespace='default', body=body)

        self.assertEqual(
            'application/strategic-merge-patch+json', self.server.content_type)
        self.assertEqual({
            'apiVersion': 'v1',
            'kind': 'ConfigMap',
            'metadata': {'name': 'sample', 'resourceVersion': '7'},
            'data': {'key': 'value'},
        }, json.loads(self.server.request_body))

    def test_builtin_list_patch_defaults_to_json_patch(self):
        body = [{'op': 'replace', 'path': '/data/key', 'value': 'changed'}]

        CoreV1Api(self.api_client).patch_namespaced_config_map(
            name='sample', namespace='default', body=body)

        self.assertEqual(
            'application/json-patch+json', self.server.content_type)
        self.assertEqual(body, json.loads(self.server.request_body))

    def test_custom_object_patch_defaults_to_merge_patch(self):
        CustomObjectsApi(self.api_client).patch_cluster_custom_object(
            group='example.com',
            version='v1',
            plural='widgets',
            name='sample',
            body={'spec': {'enabled': True}},
        )

        self.assertEqual(
            'application/merge-patch+json', self.server.content_type)
        self.assertEqual(
            '/apis/example.com/v1/widgets/sample', self.server.request_path)
        self.assertEqual(
            {'spec': {'enabled': True}}, json.loads(self.server.request_body))

    def test_custom_object_list_patch_uses_explicit_json_patch(self):
        body = [{'op': 'replace', 'path': '/spec/enabled', 'value': True}]

        CustomObjectsApi(self.api_client).patch_cluster_custom_object(
            group='example.com',
            version='v1',
            plural='widgets',
            name='sample',
            body=body,
            _content_type='application/json-patch+json',
        )

        self.assertEqual(
            'application/json-patch+json', self.server.content_type)
        self.assertEqual(body, json.loads(self.server.request_body))

    def test_create_from_yaml_supports_async_requests(self):
        manifest = {
            'apiVersion': 'v1',
            'kind': 'ConfigMap',
            'metadata': {'name': 'sample'},
        }

        created = create_from_yaml(
            self.api_client,
            yaml_objects=[manifest],
            async_req=True,
        )

        self.assertEqual(1, len(created))
        self.assertEqual(1, len(created[0]))
        self.assertIsInstance(created[0][0], ApplyResult)
        created[0][0].get(timeout=5)
        self.assertEqual(
            '/api/v1/namespaces/default/configmaps',
            self.server.request_path,
        )

    def test_watch_raises_generated_api_http_errors(self):
        self.server.response_body = b'{"message": "missing"}'
        self.server.response_status = 404

        with self.assertRaises(NotFoundException) as raised:
            list(Watch().stream(
                CoreV1Api(self.api_client).list_namespace,
                timeout_seconds=1,
            ))

        self.assertEqual(404, raised.exception.status)
        self.assertIn('missing', raised.exception.body)


if __name__ == '__main__':
    unittest.main()
