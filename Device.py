#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import json

class Device:
    def __init__(self, hostName, macAddress):
        self.macAddress = macAddress
        self.hostName = hostName
        self.date = time.strftime("%Y%m%d")

    def add(self):
        pass
