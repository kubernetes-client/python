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

import unittest

from mock import Mock

from .watch import Watch


class WatchTests(unittest.TestCase):

    def test_watch_with_decode(self):
        fake_resp = Mock()
        fake_resp.close = Mock()
        fake_resp.release_conn = Mock()
        fake_resp.read_chunked = Mock(
            return_value=[
                '{"type": "ADDED", "object": {"metadata": {"name": "test1"}'
                ',"spec": {}, "status": {}}}\n',
                '{"type": "ADDED", "object": {"metadata": {"name": "test2"}'
                ',"spec": {}, "sta',
                'tus": {}}}\n'
                '{"type": "ADDED", "object": {"metadata": {"name": "test3"},'
                '"spec": {}, "status": {}}}\n',
                'should_not_happened\n'])

        fake_api = Mock()
        fake_api.get_namespaces = Mock(return_value=fake_resp)
        fake_api.get_namespaces.__doc__ = ':return: V1NamespaceList'

        w = Watch()
        count = 1
        for e in w.stream(fake_api.get_namespaces):
            self.assertEqual("ADDED", e['type'])
            # make sure decoder worked and we got a model with the right name
            self.assertEqual("test%d" % count, e['object'].metadata.name)
            count += 1
            # make sure we can stop the watch and the last event with won't be
            # returned
            if count == 4:
                w.stop()

        fake_api.get_namespaces.assert_called_once_with(
            _preload_content=False, watch=True)
        fake_resp.read_chunked.assert_called_once_with(decode_content=False)
        fake_resp.close.assert_called_once()
        fake_resp.release_conn.assert_called_once()

    def test_unmarshal_with_float_object(self):
        w = Watch()
        event = w.unmarshal_event('{"type": "ADDED", "object": 1}', 'float')
        self.assertEqual("ADDED", event['type'])
        self.assertEqual(1.0, event['object'])
        self.assertTrue(isinstance(event['object'], float))
        self.assertEqual(1, event['raw_object'])

    def test_unmarshal_with_no_return_type(self):
        w = Watch()
        event = w.unmarshal_event('{"type": "ADDED", "object": ["test1"]}',
                                  None)
        self.assertEqual("ADDED", event['type'])
        self.assertEqual(["test1"], event['object'])
        self.assertEqual(["test1"], event['raw_object'])

    def test_watch_with_exception(self):
        fake_resp = Mock()
        fake_resp.close = Mock()
        fake_resp.release_conn = Mock()
        fake_resp.read_chunked = Mock(side_effect=KeyError('expected'))

        fake_api = Mock()
        fake_api.get_thing = Mock(return_value=fake_resp)

        w = Watch()
        try:
            for _ in w.stream(fake_api.get_thing):
                self.fail(self, "Should fail on exception.")
        except KeyError:
            pass
            # expected

        fake_api.get_thing.assert_called_once_with(
            _preload_content=False, watch=True)
        fake_resp.read_chunked.assert_called_once_with(decode_content=False)
        fake_resp.close.assert_called_once()
        fake_resp.release_conn.assert_called_once()


if __name__ == '__main__':
    unittest.main()
