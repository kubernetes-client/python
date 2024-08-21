#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
This example uses kubernetes.utils.duration to parse and display
a GEP-2257 duration string (you can find the full specification at
https://gateway-api.sigs.k8s.io/geps/gep-2257/).

Good things to try:
>>> python examples/duration-gep2257.py 1h
Duration: 1h
>>> python examples/duration-gep2257.py 3600s
Duration: 1h
>>> python examples/duration-gep2257.py 90m
Duration: 1h30m
>>> python examples/duration-gep2257.py 30m1h10s5s
Duration: 1h30m15s
>>> python examples/duration-gep2257.py 0h0m0s0ms
Duration: 0s
>>> python examples/duration-gep2257.py -5m
ValueError: Invalid duration format: -5m
>>> python examples/duration-gep2257.py 1.5h
ValueError: Invalid duration format: 1.5h
"""

import sys

from kubernetes.utils import duration

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <duration>".format(sys.argv[0]))
        sys.exit(1)

    dur = duration.parse_duration(sys.argv[1])
    print("Duration: %s" % duration.format_duration(dur))

if __name__ == "__main__":
    main()
