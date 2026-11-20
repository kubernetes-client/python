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

import unittest
from unittest import mock

from kubernetes import client

from ..leaderelectionrecord import LeaderElectionRecord
from .configmaplock import ConfigMapLock


def make_lock():
    with mock.patch.object(client, 'CoreV1Api'):
        return ConfigMapLock('lock', 'default', 'candidate')


class ConfigMapLockTest(unittest.TestCase):

    def test_leader_transitions_survive_a_write_and_read(self):
        lock = make_lock()
        record = LeaderElectionRecord('candidate', '17', '2026-08-29 01:02:03',
                                      '2026-08-29 01:02:03', 5)

        lock_dict = lock.get_lock_dict(record)
        self.assertEqual(5, lock_dict['leaderTransitions'])

        read_back = lock.get_lock_object(dict(lock_dict))
        self.assertEqual(record.__dict__, read_back.__dict__)

    def test_annotation_without_transitions_reads_as_zero(self):
        lock = make_lock()
        annotation = {'holderIdentity': 'candidate',
                      'leaseDurationSeconds': '17',
                      'acquireTime': '2026-08-29 01:02:03',
                      'renewTime': '2026-08-29 01:02:03'}

        self.assertEqual(0, lock.get_lock_object(annotation).leader_transitions)


if __name__ == '__main__':
    unittest.main()
