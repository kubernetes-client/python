import datetime
import sched
import sys
import time
import ast
import threadingWithException


class LeaderElection:
    def __init__(self, electionConfig):
        if electionConfig is None:
            sys.exit("argument config not passed")

        # The configuration set for this candidate
        self.electionConfig = electionConfig
        # The election record kept by this candidate
        self.leaderElectionRecord = None

        # updateLeaseSchedulerId variable stores the scheduler object id for the updateLease schedule that is repeated
        # every retryPeriod seconds by the leader
        self.updateLeaseSchedulerId = None

        # In terms of a leader, latestElectionObject is used to record the latest response when the lock is updated
        # In terms of a follower, latestElectionObject is used to record the latest observed lock
        self.latestElectionObject = None

        # isLeaseUpdated is used by the leader to validate lock update success, done every retryPeriod seconds
        self.isLeaseUpdated = False
        
        # followerLeaseCheckScheduler stores the scheduler object id for the checkLeaseUpdates schedule that is repeated
        # every retryPeriod seconds by the follower 
        self.followerLeaseCheckScheduler = None

        # oldElectionRecord stores the latest election record as observed by the follower
        self.oldElectionRecord = None

        # isLeaseUpdatedFollower is used by a follower candidate to mark if the leader has updated the lock object
        self.isLeaseUpdatedFollower = False
        
        # leaderFunctionThread contains the thread object for onStartedLeading
        self.leaderFunctionThread = None
        
        # OnStoppedLeadingThread contains the thread object for onStoppedLeading
        self.OnStoppedLeadingThread = None

    # For internal book-keeping
    def leaderElectorRecord(self, electionConfig):
        return {"holderIdentity": str(electionConfig.lock.identity),
                "leaseDurationSeconds": str(electionConfig.leaseDuration),
                "acquireTime": str(datetime.datetime.now())}

    # Returns latest leader
    def getLatestLeader(self):
        getStatus, getResponse = self.electionConfig.lock.Get(name=self.electionConfig.lock.name, namespace=self.electionConfig.lock.namespace)
        if getStatus:
            return "leader is " + str(ast.literal_eval(getResponse.metadata.annotations[self.electionConfig.lock.LeaderElectionRecordAnnotationKey])['holderIdentity'])
        else:
            return "could not get the latest leader"

    # Point of entry to Leader election
    def Run(self):
        # Try to create/ acquire a lock
        self.tryAcquireOrRenew()

    def tryAcquireOrRenew(self):
        # Check if lock is created
        lockStatus, lockResponse = self.electionConfig.lock.Get(self.electionConfig.lock.name, self.electionConfig.lock.namespace)

        # create a default Election record for this candidate
        self.leaderElectionRecord = self.leaderElectorRecord(self.electionConfig)

        # If a lock is already created with that name
        if lockStatus:
            print(self.electionConfig.lock.identity, "is a follower")
            scheduler_follower = sched.scheduler(time.time, time.sleep)
            self.follow(scheduler_follower)

        # A lock is not created with that name, so create one
        else:
            print(self.leaderElectionRecord['holderIdentity'], "is trying to create a lock")
            createStatus, createResponse = self.electionConfig.lock.Create(name=self.electionConfig.lock.name,
                                                                    namespace=self.electionConfig.lock.namespace,
                                                                    electionRecord=self.leaderElectionRecord)

            if createStatus is False:
                # If unable to create a lock then follow
                print(self.leaderElectionRecord['holderIdentity'], "unable to create a lock, and will be a follower")
                # Follow
                scheduler_follower = sched.scheduler(time.time, time.sleep)
                self.follow(scheduler_follower)

            else:
                # If lock is created successfully - Lead
                self.latestElectionObject = createResponse
                print(self.leaderElectionRecord['holderIdentity'], "successfully created a lock")

                # Start leading and call OnStartedLeading()
                self.leaderFunctionThread = threadingWithException.thread(self.electionConfig.onStartedLeading)
                self.leaderFunctionThread.start()

                # Schedule the function of updating the lock
                scheduler_leader = sched.scheduler(time.time, time.sleep)
                self.Lead(scheduler_leader)

    def transitionFollowerToLeader(self):
        scheduler = sched.scheduler(time.time, time.sleep)
        if self.updateLease(scheduler) is False:
            # Some other follower updated the lock
            print(self.leaderElectionRecord['holderIdentity'], "failed to lead")
            # the user is notified
            print(self.getLatestLeader())
            # A new leader has been established
            self.follow(scheduler)
        else:
            # Make sure thread that runs onStoppedLeading callback is stopped
            if self.OnStoppedLeadingThread:
                self.OnStoppedLeadingThread.stop()
                self.OnStoppedLeadingThread.join()

            # this candidate starts leading
            self.leaderFunctionThread = threadingWithException.thread(self.electionConfig.onStartedLeading)
            self.leaderFunctionThread.start()
            self.Lead(scheduler)

    def Lead(self, scheduler):
        # Leader functions
        # updateLease function updates the lock in intervals of retryPeriod seconds
        self.updateLeaseSchedulerId = scheduler.enter(0, 1, self.updateLease, (scheduler,))
        # checkLeaseHealth reports unhealthy if the leader fails to update the lock during a complete renewDealine
        # period
        scheduler.enter(int(self.electionConfig.renewDeadline), 1, self.checkLeaseHealth, (scheduler,))
        scheduler.run()

    def checkLeaseHealth(self, scheduler):
        # Leader
        print("Leader lease update status during the complete renewDeadline:", self.isLeaseUpdated)
        # At the end of each renewDeadline check if the lock was updated, if yes then set the update check variable to False and keep leading
        if self.isLeaseUpdated is True:
            self.isLeaseUpdated = False
            scheduler.enter(int(self.electionConfig.renewDeadline), 1, self.checkLeaseHealth, (scheduler,))
        else:
            # The leader failed to update lease, and the leader stops updating the lock
            if self.updateLeaseSchedulerId:
                scheduler.cancel(self.updateLeaseSchedulerId)
                self.updateLeaseSchedulerId = None

            # kill the OnLeading callback
            self.leaderFunctionThread.stop()
            self.leaderFunctionThread.join()

            # create OnStoppedLeading thread
            self.OnStoppedLeadingThread = threadingWithException.thread(self.electionConfig.onStoppedLeading)
            self.OnStoppedLeadingThread.start()

            # Start to follow
            self.follow(scheduler)

    def updateLease(self, scheduler):
        # Leader
        # Get the election record from the latest lock object
        ElectionRecord = ast.literal_eval(self.latestElectionObject.metadata.annotations[self.electionConfig.lock.LeaderElectionRecordAnnotationKey])

        # Update time and identity
        ElectionRecord['acquireTime'] = str(datetime.datetime.now())
        ElectionRecord['holderIdentity'] = str(self.electionConfig.lock.identity)

        # Set the latestElectionObject with the latest election record 
        self.latestElectionObject.metadata.annotations[self.electionConfig.lock.LeaderElectionRecordAnnotationKey] = str(ElectionRecord)
        
        updateStatus, updateResponse = self.electionConfig.lock.Update(self.electionConfig.lock.name, self.electionConfig.lock.namespace, self.latestElectionObject)
        
        # lock was successfully updated by the leader
        if updateStatus:
            self.isLeaseUpdated = True
            self.latestElectionObject = updateResponse
            # Continue updating lease every retyPeriod seconds
            self.updateLeaseSchedulerId = scheduler.enter(int(self.electionConfig.retryPeriod), 1, self.updateLease, (scheduler,))
        else:
            self.isLeaseUpdated = False
            # Might encounter this only when a follower is trying to acquire a lock to gain leadership
            # but another candidate got their first and updated the lock
            return False

    def follow(self, scheduler):
        # checkLeaseUpdates checks if the lock object is updated by the leader, every retryPeriod seconds
        self.followerLeaseCheckScheduler = scheduler.enter(0, 1, self.checkLeaseUpdates, (scheduler,))

        # checkLeaseUpdateHealth checks if the leader could update the lock object during a complete leaseDuration
        scheduler.enter(int(self.electionConfig.leaseDuration), 1, self.checkLeaseUpdateHealth, (scheduler,))
        scheduler.run()

    def checkLeaseUpdateHealth(self, scheduler):
        # Follower
        if self.isLeaseUpdatedFollower is True:
            # That means the leader was able to update the lock and the changes were recorded by the follower
            print("Follower checking Leader lease update - status:", self.isLeaseUpdatedFollower)
            self.isLeaseUpdatedFollower = False
            # keep checking lease update health after every leaseDuration seconds
            scheduler.enter(int(self.electionConfig.leaseDuration), 1, self.checkLeaseUpdateHealth, (scheduler,))
        else:
            # Leader has failed to update Lease and the follower has identified this
            if self.followerLeaseCheckScheduler:
                scheduler.cancel(self.followerLeaseCheckScheduler)
                self.followerLeaseCheckScheduler = None
            self.transitionFollowerToLeader()

    def checkLeaseUpdates(self, scheduler):
        # Follower
        # if oldElectionRecord is uninitialized then this is the first time this follower is checking for lease updates
        if self.oldElectionRecord is None:
            getStatus,  getResponse = self.electionConfig.lock.Get(self.electionConfig.lock.name, self.electionConfig.lock.namespace)
            self.oldElectionRecord = ast.literal_eval(getResponse.metadata.annotations[self.electionConfig.lock.LeaderElectionRecordAnnotationKey])

            # keep checking lease updates every retryPeriod seconds
            self.followerLeaseCheckScheduler = scheduler.enter(int(self.electionConfig.retryPeriod), 1, self.checkLeaseUpdates, (scheduler,))
        else:
            getStatus, getResponse = self.electionConfig.lock.Get(self.electionConfig.lock.name, self.electionConfig.lock.namespace)

            # store the latest lock object
            self.latestElectionObject = getResponse

            # get the latest election record
            currentElectionRecord = ast.literal_eval(getResponse.metadata.annotations[self.electionConfig.lock.LeaderElectionRecordAnnotationKey])

            if self.oldElectionRecord['holderIdentity'] != currentElectionRecord['holderIdentity']:
                print("New leader is ", currentElectionRecord['holderIdentity'])

            # compare timestamps
            if self.oldElectionRecord['acquireTime'] != currentElectionRecord['acquireTime']:
                # Leader has updated lease continue following
                self.isLeaseUpdatedFollower = True

            self.oldElectionRecord = currentElectionRecord


            # keep checking for lease updates every retryPeriod seconds
            self.followerLeaseCheckScheduler = scheduler.enter(int(self.electionConfig.retryPeriod), 1, self.checkLeaseUpdates, (scheduler,))
