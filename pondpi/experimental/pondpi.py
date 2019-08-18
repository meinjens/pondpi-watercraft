#!/usr/bin/env python
# coding: latin-1

import pigpio


class L298NHBridge:
    def __init__(self):
        pass


if __name__ == "__main__":
    print("start")

    pi = pigpio.pi()

    print("init")

    pi.stop()
