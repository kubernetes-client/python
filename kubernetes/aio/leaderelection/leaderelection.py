# Copyright 2021 The Kubernetes Authors.
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

import asyncio
import datetime
import json
import logging
import sys
import time
from http import HTTPStatus

from kubernetes.aio.client.exceptions import ApiException
from kubernetes.aio.leaderelection.electionconfig import Config
from kubernetes.aio.leaderelection.leaderelectionrecord import (
    LeaderElectionRecord,
)

logger = logging.getLogger(__name__)

"""
This package implements leader election using an annotation in a Kubernetes
object. The onstarted_leading coroutine is run as a task, which is cancelled if
the leader lock is obtained and then lost.

At first all candidates are considered followers. The one to create a lock or
update an existing lock first becomes the leader and remains so until it fails
to renew its lease.
"""


class LeaderElection:
    def __init__(self, election_config: Config) -> None:
        if election_config is None:
            sys.exit("argument config not passed")

        # Latest record observed in the created lock object
        self.observed_record: LeaderElectionRecord | None = None

        # The configuration set for this candidate
        self.election_config: Config = election_config

        # Latest update time of the lock
        self.observed_time_milliseconds = 0

    # Point of entry to Leader election
    async def run(self) -> None:
        # Try to create/ acquire a lock
        if await self.acquire():
            logger.info(
                "%s successfully acquired lease", self.election_config.lock.identity
            )

            onstarted_leading_coroutine = (
                self.election_config.onstarted_leading()
                if callable(self.election_config.onstarted_leading)
                else self.election_config.onstarted_leading
            )

            task = asyncio.create_task(onstarted_leading_coroutine)

            await self.renew_loop()

            # Leader lock lost - cancel the onstarted_leading coroutine if it's
            # still running. This permits onstarted_leading to clean up state
            # that might not be accessible to onstopped_leading.
            task.cancel()

            # Failed to update lease, run onstopped_leading callback. This is
            # preserved in order to continue to provide an interface similar to
            # the one provided by `kubernetes-client/python`.
            if self.election_config.onstopped_leading is not None:
                await (
                    self.election_config.onstopped_leading()
                    if callable(self.election_config.onstopped_leading)
                    else self.election_config.onstopped_leading
                )

    async def acquire(self) -> bool:
        # Follower
        logger.debug("%s is a follower", self.election_config.lock.identity)
        retry_period = self.election_config.retry_period

        while True:
            succeeded = await self.try_acquire_or_renew()

            if succeeded:
                return True

            await asyncio.sleep(retry_period)

    async def renew_loop(self) -> None:
        # Leader
        logger.debug(
            "Leader has entered renew loop and will try to update lease continuously"
        )

        retry_period = self.election_config.retry_period
        renew_deadline = self.election_config.renew_deadline * 1000

        while True:
            timeout = int(time.time() * 1000) + renew_deadline
            succeeded = False

            while int(time.time() * 1000) < timeout:
                succeeded = await self.try_acquire_or_renew()

                if succeeded:
                    break
                await asyncio.sleep(retry_period)

            if succeeded:
                await asyncio.sleep(retry_period)
                continue

            # failed to renew, return
            return

    async def try_acquire_or_renew(self) -> bool:
        now_timestamp = time.time()
        now = datetime.datetime.fromtimestamp(now_timestamp)

        # Check if lock is created
        lock_status, old_election_record = await self.election_config.lock.get(
            self.election_config.lock.name, self.election_config.lock.namespace
        )

        # create a default Election record for this candidate
        leader_election_record = LeaderElectionRecord(
            self.election_config.lock.identity,
            str(self.election_config.lease_duration),
            str(now),
            str(now),
        )

        # A lock is not created with that name, try to create one
        if not lock_status:
            assert (
                isinstance(old_election_record, ApiException)
                and old_election_record.body is not None
            )
            if json.loads(old_election_record.body)["code"] != HTTPStatus.NOT_FOUND:
                logger.error(
                    "Error retrieving resource lock %s as %s",
                    self.election_config.lock.name,
                    old_election_record.reason,
                )
                return False

            logger.debug(
                "%s is trying to create a lock",
                leader_election_record.holder_identity,
            )
            create_status = await self.election_config.lock.create(
                name=self.election_config.lock.name,
                namespace=self.election_config.lock.namespace,
                election_record=leader_election_record,
            )

            if not create_status:
                logger.error(
                    "%s failed to create lock", leader_election_record.holder_identity
                )
                return False

            self.observed_record = leader_election_record
            self.observed_time_milliseconds = int(time.time() * 1000)
            return True

        # A lock exists with that name
        # Validate old_election_record
        if old_election_record is None:
            # try to update lock with proper election record
            return await self.update_lock(leader_election_record)

        assert isinstance(old_election_record, LeaderElectionRecord)
        if (
            old_election_record.holder_identity is None
            or old_election_record.lease_duration is None
            or old_election_record.acquire_time is None
            or old_election_record.renew_time is None
        ):
            # try to update lock with proper election record
            return await self.update_lock(leader_election_record)

        # Report transitions
        if (
            self.observed_record
            and self.observed_record.holder_identity
            != old_election_record.holder_identity
        ):
            logger.debug(
                "Leader has switched to %s", old_election_record.holder_identity
            )

        if (
            self.observed_record is None
            or old_election_record.__dict__ != self.observed_record.__dict__
        ):
            self.observed_record = old_election_record
            self.observed_time_milliseconds = int(time.time() * 1000)

        # If This candidate is not the leader and lease duration is yet to finish
        if (
            self.election_config.lock.identity != self.observed_record.holder_identity
            and self.observed_time_milliseconds
            + self.election_config.lease_duration * 1000
            > int(now_timestamp * 1000)
        ):
            logger.debug(
                "Yet to finish lease_duration, lease held by %s and has not expired",
                old_election_record.holder_identity,
            )
            return False

        # If this candidate is the Leader
        if self.election_config.lock.identity == self.observed_record.holder_identity:
            # Leader updates renewTime, but keeps acquire_time unchanged
            leader_election_record.acquire_time = self.observed_record.acquire_time

        return await self.update_lock(leader_election_record)

    async def update_lock(self, leader_election_record: LeaderElectionRecord) -> bool:
        # Update object with latest election record
        update_status = await self.election_config.lock.update(
            self.election_config.lock.name,
            self.election_config.lock.namespace,
            leader_election_record,
        )

        if not update_status:
            logger.warning(
                "%s failed to acquire lease", leader_election_record.holder_identity
            )
            return False

        self.observed_record = leader_election_record
        self.observed_time_milliseconds = int(time.time() * 1000)
        logger.debug(
            "Leader %s has successfully updated lease",
            leader_election_record.holder_identity,
        )
        return True
