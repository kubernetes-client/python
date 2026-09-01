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

from kubernetes.client.rest import ApiException
from kubernetes import client
from ..leaderelectionrecord import LeaderElectionRecord
from datetime import datetime, timezone
import logging
logger = logging.getLogger("leaderelection")

# Formats produced by str(datetime). The microsecond component is omitted
# when it is exactly zero, so both spellings have to be accepted.
TIME_FORMATS = (
    "%Y-%m-%d %H:%M:%S.%f%z",
    "%Y-%m-%d %H:%M:%S.%f",
    "%Y-%m-%d %H:%M:%S%z",
    "%Y-%m-%d %H:%M:%S",
)


class LeaseLock:
    def __init__(self, name, namespace, identity):
        """
        :param name: name of the lock
        :param namespace: namespace
        :param identity: A unique identifier that the candidate is using
        """
        self.api_instance = client.CoordinationV1Api()
        self.name = name
        self.namespace = namespace
        self.identity = str(identity)
        self.lease_reference = None

    # get returns the election record from a Lease spec
    def get(self, name, namespace):
        """
        :param name: Name of the lease object information to get
        :param namespace: Namespace in which the lease object is to be searched
        :return: 'True, election record' if object found else 'False, exception response'
        """
        try:
            lease = self.api_instance.read_namespaced_lease(name, namespace)
        except ApiException as e:
            return False, e

        self.lease_reference = lease
        return True, self.get_lock_object(lease)

    def create(self, name, namespace, election_record):
        """
        :param name: Name of the lease object to be created
        :param namespace: Namespace in which the lease object is to be created
        :param election_record: The election record to store in the lease spec
        :return: 'True' if object is created else 'False' if failed
        """
        body = client.V1Lease(metadata={"name": name},
                              spec=self.get_lease_spec(election_record))

        try:
            # Keep the created lease so that a following update has a
            # reference to work from without re-reading it.
            self.lease_reference = self.api_instance.create_namespaced_lease(
                namespace, body)
            return True
        except ApiException as e:
            logger.info("Failed to create lock as {}".format(e))
            return False

    def update(self, name, namespace, updated_record):
        """
        :param name: name of the lock to be updated
        :param namespace: namespace the lock is in
        :param updated_record: the updated election record
        :return: True if update is successful False if it fails
        """
        if self.lease_reference is None:
            logger.info("Lease not initialized, call get or create first")
            return False

        try:
            self.lease_reference.spec = self.get_lease_spec(
                updated_record, self.lease_reference.spec)
            self.api_instance.replace_namespaced_lease(
                name=name, namespace=namespace, body=self.lease_reference)
            return True
        except ApiException as e:
            logger.info("Failed to update lock as {}".format(e))
            return False

    def get_lease_spec(self, leader_election_record, current_spec=None):
        """Build the lease spec that holds the given election record."""
        spec = current_spec if current_spec else client.V1LeaseSpec()

        spec.holder_identity = leader_election_record.holder_identity
        spec.lease_duration_seconds = int(leader_election_record.lease_duration)
        spec.acquire_time = self.time_str_to_iso(
            leader_election_record.acquire_time)
        spec.renew_time = self.time_str_to_iso(
            leader_election_record.renew_time)

        return spec

    def get_lock_object(self, lease):
        """Build the election record held in the given lease spec."""
        leader_election_record = LeaderElectionRecord(None, None, None, None)

        if not lease.spec:
            return leader_election_record

        if lease.spec.holder_identity:
            leader_election_record.holder_identity = lease.spec.holder_identity
        if lease.spec.lease_duration_seconds:
            leader_election_record.lease_duration = str(
                lease.spec.lease_duration_seconds)
        if lease.spec.acquire_time:
            leader_election_record.acquire_time = self.time_from_utc(
                lease.spec.acquire_time)
        if lease.spec.renew_time:
            leader_election_record.renew_time = self.time_from_utc(
                lease.spec.renew_time)

        return leader_election_record

    def time_str_to_iso(self, str_time):
        """Convert an election record time into the instant to store.

        ``leaderelection.py`` builds its times with
        ``datetime.fromtimestamp()``, which is local and naive. The Lease is
        shared with other clients, so the value has to go on the wire as the
        real UTC instant rather than as local wall clock labeled as UTC.
        """
        for fmt in TIME_FORMATS:
            try:
                parsed = datetime.strptime(str_time, fmt)
            except ValueError:
                continue
            if parsed.tzinfo is None:
                parsed = parsed.astimezone()
            return parsed.astimezone(timezone.utc)
        raise ValueError("Failed to parse time string: {}".format(str_time))

    def time_from_utc(self, value):
        """Inverse of :meth:`time_str_to_iso`, back to the record format."""
        return str(value.astimezone().replace(tzinfo=None))
