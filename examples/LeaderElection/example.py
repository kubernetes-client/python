import uuid
import LeaderElection
from kubernetes import client, config
from resourcelock.ConfigMapLock import ConfigMapLock
import Config
from datetime import timedelta

# Authenticate using config file
config.load_kube_config(config_file=r"")

# Variables required from the user
# A unique identifier
candidate_id = uuid.uuid4()

# Name of the locking object to be created
LockName = "examplepython"

# Object namespace
LockNameSpace = "default"


# The function that you want to run once a candidate is elected as a leader
def example_func():
    print("I am leader")


# Create config, a user can choose not to provide any callbacks for what to do when a candidate fails to lead - onStoppedLeading()
# , if the default callback function will be used is a callback is not provide
config = Config.createConfig(ConfigMapLock(LockName, LockNameSpace, candidate_id), leaseDuration=17, renewDeadline=15, retryPeriod=5, onStartedLeading=example_func, onStoppedLeading=None)

LeaderElection.LeaderElection(config).Run()

