import sys


class createConfig:
    # Validate config, exit if an error is detected
    def __init__(self, lock, leaseDuration, renewDeadline, retryPeriod, onStartedLeading, onStoppedLeading):
        self.JitterFactor = 1.2

        if lock is None:
            sys.exit("lock cannot be None")
        self.lock = lock

        if leaseDuration <= renewDeadline:
            sys.exit("leaseDuration must be greater than renewDeadline")

        if renewDeadline <= self.JitterFactor * retryPeriod:
            sys.exit("leaseDuration must be greater than renewDeadline")

        if leaseDuration < 1:
            sys.exit("leaseDuration must be greater than zero")

        if renewDeadline < 1:
            sys.exit("renewDeadline must be greater than zero")

        if retryPeriod < 1:
            sys.exit("retryPeriod must be greater than zero")

        self.leaseDuration = leaseDuration
        self.renewDeadline = renewDeadline
        self.retryPeriod = retryPeriod

        if onStartedLeading is None:
            sys.exit("callback onStartedLeading cannot be None")
        self.onStartedLeading = onStartedLeading

        if onStoppedLeading is None:
            self.onStoppedLeading = self.onStoppedLeadingCallback
        else:
            self.onStoppedLeading = onStoppedLeading

    # Default callback for when the current candidate if a leader, stops leading
    def onStoppedLeadingCallback(self):
        print(self.lock.identity, "stopped leading")