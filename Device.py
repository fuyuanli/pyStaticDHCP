#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import json
import codecs

class Device:
    def __init__(self, hostname, macaddress, days):
        self.macaddress = macaddress
        self.hostname = hostname
        self.date = time.strftime("%Y%m%d")
        self.days = days

    def getDate(self):
        return self.date

    def getDays(self):
        return self.days

    def getHost(self):
        return self.hostname

    def getMac(self):
        return self.macaddress

    def add(self):
        check = 0
        newDevice = {
            "signup": self.getDate(),
            "days": self.getDays(),
            "hostname": self.getHost(),
            "macaddress": self.getMac(),
        }

        with codecs.open('macs.json', 'r+', encoding='utf-8') as f:
            data = json.load(f)

            for i in range(len(data)):
                if data[i]["hostname"] == self.getHost:
                    print("[Error] hostname 已存在 !!")
                    check = 1

                if data[i]["macaddress"] == self.getMac:
                     print("[Error] mac address 已存在 !!")
                     check = 1

            if check == 0:
                data.append(newDevice)
                f.seek(0)
                json.dump(data, f, indent=4)
                print("[Success] 寫入完成")
            else:
                print("[Error] 資料錯誤，略過寫入 !!")
