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
import json
import unittest
from collections.abc import Callable
from unittest import IsolatedAsyncioTestCase

from kubernetes.aio.client.rest import ApiException
from kubernetes.aio.leaderelection import electionconfig, leaderelection
from kubernetes.aio.leaderelection.leaderelectionrecord import (
    LeaderElectionRecord,
)
from kubernetes.aio.leaderelection.resourcelock.baselock import BaseLock


class LeaderElectionTest(IsolatedAsyncioTestCase):
    async def test_simple_leader_election(self) -> None:
        election_history = []
        leadership_history = []

        def on_create():
            election_history.append("create record")
            leadership_history.append("get leadership")

        def on_update():
            election_history.append("update record")

        def on_change():
            election_history.append("change record")

        mock_lock = MockResourceLock(
            "mock",
            "mock_namespace",
            "mock",
            asyncio.Lock(),
            on_create,
            on_update,
            on_change,
            None,
        )

        async def on_started_leading() -> None:
            leadership_history.append("start leading")

        async def on_stopped_leading() -> None:
            leadership_history.append("stop leading")

        # Create config 4.5 4 3
        config = electionconfig.Config(
            lock=mock_lock,
            lease_duration=2.5,
            renew_deadline=2,
            retry_period=1.5,
            onstarted_leading=on_started_leading(),
            onstopped_leading=on_stopped_leading(),
        )

        # Enter leader election
        await leaderelection.LeaderElection(config).run()

        self.assert_history(
            election_history,
            ["create record", "update record", "update record", "update record"],
        )
        self.assert_history(
            leadership_history, ["get leadership", "start leading", "stop leading"]
        )

    async def test_leader_election(self) -> None:
        election_history = []
        leadership_history = []

        def on_create_A():
            election_history.append("A creates record")
            leadership_history.append("A gets leadership")

        def on_update_A():
            election_history.append("A updates record")

        def on_change_A():
            election_history.append("A gets leadership")

        lock = asyncio.Lock()

        mock_lock_A = MockResourceLock(
            "mock",
            "mock_namespace",
            "MockA",
            lock,
            on_create_A,
            on_update_A,
            on_change_A,
            None,
        )
        mock_lock_A.renew_count_max = 3

        async def on_started_leading_A():
            leadership_history.append("A starts leading")

        async def on_stopped_leading_A():
            leadership_history.append("A stops leading")

        config_A = electionconfig.Config(
            lock=mock_lock_A,
            lease_duration=2.5,
            renew_deadline=2,
            retry_period=1.5,
            onstarted_leading=on_started_leading_A(),
            onstopped_leading=on_stopped_leading_A(),
        )

        def on_create_B():
            election_history.append("B creates record")
            leadership_history.append("B gets leadership")

        def on_update_B():
            election_history.append("B updates record")

        def on_change_B():
            leadership_history.append("B gets leadership")

        mock_lock_B = MockResourceLock(
            "mock",
            "mock_namespace",
            "MockB",
            lock,
            on_create_B,
            on_update_B,
            on_change_B,
            None,
        )
        mock_lock_B.renew_count_max = 4

        async def on_started_leading_B():
            leadership_history.append("B starts leading")

        async def on_stopped_leading_B():
            leadership_history.append("B stops leading")

        config_B = electionconfig.Config(
            lock=mock_lock_B,
            lease_duration=2.5,
            renew_deadline=2,
            retry_period=1.5,
            onstarted_leading=on_started_leading_B(),
            onstopped_leading=on_stopped_leading_B(),
        )

        mock_lock_B.leader_record = mock_lock_A.leader_record

        config_A_election = asyncio.create_task(
            leaderelection.LeaderElection(config_A).run()
        )
        config_B_election = asyncio.create_task(
            leaderelection.LeaderElection(config_B).run()
        )

        await asyncio.gather(config_A_election, config_B_election)

        self.assert_history(
            election_history,
            [
                "A creates record",
                "A updates record",
                "A updates record",
                "B updates record",
                "B updates record",
                "B updates record",
                "B updates record",
            ],
        )
        self.assert_history(
            leadership_history,
            [
                "A gets leadership",
                "A starts leading",
                "A stops leading",
                "B gets leadership",
                "B starts leading",
                "B stops leading",
            ],
        )

    """Expected behavior: to check if the leader stops leading if it fails to update the lock within the renew_deadline
    and stops leading after finally timing out. The difference between each try comes out to be approximately the sleep
    time.
    Example:
    create record:  0s
    on try update:  1.5s
    on update:  zzz s
    on try update:  3s
    on update: zzz s
    on try update:  4.5s
    on try update:  6s
    Timeout - Leader Exits"""

    async def test_leader_election_with_renew_deadline(self) -> None:
        election_history = []
        leadership_history = []

        def on_create():
            election_history.append("create record")
            leadership_history.append("get leadership")

        def on_update():
            election_history.append("update record")

        def on_change():
            election_history.append("change record")

        def on_try_update():
            election_history.append("try update record")

        mock_lock = MockResourceLock(
            "mock",
            "mock_namespace",
            "mock",
            asyncio.Lock(),
            on_create,
            on_update,
            on_change,
            on_try_update,
        )
        mock_lock.renew_count_max = 3

        async def on_started_leading():
            leadership_history.append("start leading")

        async def on_stopped_leading():
            leadership_history.append("stop leading")

        # Create config
        config = electionconfig.Config(
            lock=mock_lock,
            lease_duration=2.5,
            renew_deadline=2,
            retry_period=1.5,
            onstarted_leading=on_started_leading(),
            onstopped_leading=on_stopped_leading(),
        )

        # Enter leader election
        await leaderelection.LeaderElection(config).run()

        self.assert_history(
            election_history,
            [
                "create record",
                "try update record",
                "update record",
                "try update record",
                "update record",
                "try update record",
                "try update record",
            ],
        )

        self.assert_history(
            leadership_history, ["get leadership", "start leading", "stop leading"]
        )

    def assert_history(self, history, expected) -> None:
        self.assertIsNotNone(expected)
        self.assertIsNotNone(history)
        self.assertEqual(len(expected), len(history))

        for idx in range(len(history)):
            self.assertEqual(
                history[idx],
                expected[idx],
                msg=f"Not equal at index {idx}, expected {expected[idx]}, got {history[idx]}",
            )


class MockResourceLock(BaseLock):
    def __init__(
        self,
        name: str,
        namespace: str,
        identity: str,
        shared_lock: asyncio.Lock,
        on_create: Callable,
        on_update: Callable,
        on_change: Callable,
        on_try_update: Callable | None,
    ) -> None:
        # self.leader_record is shared between two MockResourceLock objects
        self.leader_record: list[LeaderElectionRecord] = []
        self.renew_count = 0
        self.renew_count_max = 4
        self.name = name
        self.namespace = namespace
        self.identity = str(identity)
        self.lock = shared_lock

        self.on_create = on_create
        self.on_update = on_update
        self.on_change = on_change
        self.on_try_update = on_try_update

    async def get(
        self, name: str, namespace: str
    ) -> tuple[bool, LeaderElectionRecord] | tuple[bool, Exception] | tuple[bool, None]:
        await self.lock.acquire()
        try:
            if self.leader_record:
                return True, self.leader_record[0]

            ex = ApiException()
            ex.body = json.dumps({"code": 404}).encode()
            return False, ex
        finally:
            self.lock.release()

    async def create(
        self, name: str, namespace: str, election_record: LeaderElectionRecord
    ) -> bool:
        await self.lock.acquire()
        try:
            if len(self.leader_record) == 1:
                return False
            self.leader_record.append(election_record)
            self.on_create()
            self.renew_count += 1
            return True
        finally:
            self.lock.release()

    async def update(
        self, name: str, namespace: str, updated_record: LeaderElectionRecord
    ) -> bool:
        await self.lock.acquire()
        try:
            if self.on_try_update:
                self.on_try_update()
            if self.renew_count >= self.renew_count_max:
                return False

            old_record = self.leader_record[0]
            self.leader_record[0] = updated_record

            self.on_update()

            if old_record.holder_identity != updated_record.holder_identity:
                await asyncio.sleep(2)
                self.on_change()

            self.renew_count += 1
            return True
        finally:
            self.lock.release()


    def test_acquire_survives_non_json_error_body(self):
        """A proxy answering with an HTML error page must not kill the elector."""

        class GatewayErrorLock:
            def __init__(self):
                self.name = "lock"
                self.namespace = "ns"
                self.identity = "candidate"

            async def get(self, name, namespace):
                return False, ApiException(
                    status=502,
                    reason="Bad Gateway",
                    body="<html><body>502 Bad Gateway</body></html>",
                )

            async def create(self, name, namespace, election_record):
                return False

        config = electionconfig.Config(
            lock=GatewayErrorLock(),
            lease_duration=4,
            renew_deadline=3,
            retry_period=1,
            onstarted_leading=lambda: None,
            onstopped_leading=lambda: None,
        )

        elector = leaderelection.LeaderElection(config)
        result = asyncio.run(elector.try_acquire_or_renew())
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
