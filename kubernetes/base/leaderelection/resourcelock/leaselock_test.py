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

import datetime
import os
import time
import unittest
from unittest import mock

from kubernetes import client
from kubernetes.client.rest import ApiException

from ..leaderelectionrecord import LeaderElectionRecord
from .leaselock import LeaseLock


def make_lock():
    with mock.patch.object(client, 'CoordinationV1Api'):
        lock = LeaseLock('lock', 'default', 'candidate')
    lock.api_instance = mock.MagicMock()
    return lock


UTC = datetime.timezone.utc


class LeaseLockTest(unittest.TestCase):

    def test_create_writes_the_election_record_to_the_spec(self):
        lock = make_lock()
        record = LeaderElectionRecord('candidate', '17',
                                      '2026-08-29 01:02:03.456789',
                                      '2026-08-29 01:02:03.456789')

        self.assertTrue(lock.create('lock', 'default', record))

        namespace, body = lock.api_instance.create_namespaced_lease.call_args[0]
        self.assertEqual('default', namespace)
        self.assertEqual('lock', body.metadata.name)
        self.assertEqual('candidate', body.spec.holder_identity)
        self.assertEqual(17, body.spec.lease_duration_seconds)
        # stored as UTC on the wire, denoting the same instant as the
        # local wall clock the election record carries
        self.assertEqual(UTC, body.spec.acquire_time.tzinfo)
        self.assertEqual('2026-08-29 01:02:03.456789',
                         str(body.spec.acquire_time.astimezone()
                             .replace(tzinfo=None)))
        self.assertEqual(body.spec.acquire_time, body.spec.renew_time)

    def test_create_returns_false_when_the_api_fails(self):
        lock = make_lock()
        lock.api_instance.create_namespaced_lease.side_effect = ApiException(
            status=409, reason='Conflict')
        record = LeaderElectionRecord('candidate', '17', '2026-08-29 01:02:03',
                                      '2026-08-29 01:02:03')

        self.assertFalse(lock.create('lock', 'default', record))

    def test_get_returns_the_exception_when_the_lease_is_missing(self):
        lock = make_lock()
        expected = ApiException(status=404, reason='Not Found')
        lock.api_instance.read_namespaced_lease.side_effect = expected

        status, response = lock.get('lock', 'default')

        self.assertFalse(status)
        self.assertIs(expected, response)

    def test_get_reads_the_election_record_from_the_lease(self):
        lock = make_lock()
        acquired = datetime.datetime(2026, 8, 29, 1, 2, 3, 456789)
        lock.api_instance.read_namespaced_lease.return_value = client.V1Lease(
            metadata={'name': 'lock'},
            spec=client.V1LeaseSpec(holder_identity='candidate',
                                    lease_duration_seconds=17,
                                    acquire_time=acquired,
                                    renew_time=acquired))

        status, record = lock.get('lock', 'default')

        self.assertTrue(status)
        self.assertEqual('candidate', record.holder_identity)
        self.assertEqual('17', record.lease_duration)
        self.assertEqual('2026-08-29 01:02:03.456789', record.acquire_time)

    def test_get_on_a_lease_without_a_spec_returns_an_empty_record(self):
        lock = make_lock()
        lock.api_instance.read_namespaced_lease.return_value = client.V1Lease(
            metadata={'name': 'lock'}, spec=None)

        status, record = lock.get('lock', 'default')

        self.assertTrue(status)
        self.assertIsNone(record.holder_identity)

    def test_record_survives_a_write_and_read_unchanged(self):
        """leaderelection.py compares the stored record with the observed one
        using __dict__, so a round trip has to come back identical."""
        lock = make_lock()
        now = datetime.datetime.fromtimestamp(1787000000.5)
        record = LeaderElectionRecord('candidate', str(17), str(now), str(now))

        spec = lock.get_lease_spec(record)
        read_back = lock.get_lock_object(
            client.V1Lease(metadata={'name': 'lock'}, spec=spec))

        self.assertEqual(record.__dict__, read_back.__dict__)

    def test_record_without_microseconds_survives_a_write_and_read(self):
        """str(datetime) drops the microseconds when they are exactly zero."""
        lock = make_lock()
        now = datetime.datetime(2026, 8, 29, 1, 2, 3)
        self.assertEqual('2026-08-29 01:02:03', str(now))
        record = LeaderElectionRecord('candidate', str(17), str(now), str(now))

        spec = lock.get_lease_spec(record)
        read_back = lock.get_lock_object(
            client.V1Lease(metadata={'name': 'lock'}, spec=spec))

        self.assertEqual(record.__dict__, read_back.__dict__)

    def test_update_replaces_the_lease_it_read(self):
        lock = make_lock()
        acquired = datetime.datetime(2026, 8, 29, 1, 2, 3, 456789)
        lock.api_instance.read_namespaced_lease.return_value = client.V1Lease(
            metadata={'name': 'lock'},
            spec=client.V1LeaseSpec(holder_identity='other',
                                    lease_duration_seconds=17,
                                    acquire_time=acquired,
                                    renew_time=acquired))
        lock.get('lock', 'default')

        record = LeaderElectionRecord('candidate', '17',
                                      '2026-08-29 01:02:03.456789',
                                      '2026-08-29 02:03:04.567890')
        self.assertTrue(lock.update('lock', 'default', record))

        body = lock.api_instance.replace_namespaced_lease.call_args[1]['body']
        self.assertEqual('candidate', body.spec.holder_identity)
        self.assertEqual('2026-08-29 02:03:04.567890',
                         str(body.spec.renew_time.astimezone()
                             .replace(tzinfo=None)))

    def test_update_returns_false_when_the_api_fails(self):
        lock = make_lock()
        lock.lease_reference = client.V1Lease(metadata={'name': 'lock'},
                                              spec=client.V1LeaseSpec())
        lock.api_instance.replace_namespaced_lease.side_effect = ApiException(
            status=409, reason='Conflict')
        record = LeaderElectionRecord('candidate', '17', '2026-08-29 01:02:03',
                                      '2026-08-29 01:02:03')

        self.assertFalse(lock.update('lock', 'default', record))

    @unittest.skipUnless(hasattr(time, 'tzset'), 'requires tzset')
    def test_times_are_written_as_the_real_utc_instant(self):
        """The election record holds local wall clock. The Lease is shared
        with other clients, so it has to carry the real UTC instant."""
        lock = make_lock()
        previous = os.environ.get('TZ')
        os.environ['TZ'] = 'Asia/Kolkata'  # UTC+05:30, no DST
        time.tzset()
        try:
            record = LeaderElectionRecord('candidate', '17',
                                          '2026-08-29 01:02:03.456789',
                                          '2026-08-29 01:02:03.456789')
            spec = lock.get_lease_spec(record)

            self.assertEqual(
                datetime.datetime(2026, 8, 28, 19, 32, 3, 456789, tzinfo=UTC),
                spec.acquire_time)
            # and it still round trips back to the local wall clock
            read_back = lock.get_lock_object(
                client.V1Lease(metadata={'name': 'lock'}, spec=spec))
            self.assertEqual(record.__dict__, read_back.__dict__)
        finally:
            if previous is None:
                os.environ.pop('TZ', None)
            else:
                os.environ['TZ'] = previous
            time.tzset()

    def test_update_before_get_or_create_does_not_raise(self):
        lock = make_lock()
        record = LeaderElectionRecord('candidate', '17', '2026-08-29 01:02:03',
                                      '2026-08-29 01:02:03')

        self.assertFalse(lock.update('lock', 'default', record))

    def test_an_unparsable_time_is_reported(self):
        lock = make_lock()
        with self.assertRaises(ValueError):
            lock.time_str_to_iso('not a time')


if __name__ == '__main__':
    unittest.main()
