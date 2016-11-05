#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import json
import codecs

class Device:
    def __init__(self):
        self.timestamp = int(time.time())

    def checkDays(self):
        with open('users.json', 'r') as f:
            data = json.load(f)
            avtive = []
            for i in range(len(data)):
                if (data[i]["signup"] + data[i]["days"]*24*60*60) > self.timestamp:
                    avtive.append(data[i])
                else:
                    print("裝置",data[i]["hostname"],data[i]["macaddress"],"使用期限已到，刪除紀錄")

        with open('users.json', 'w') as f:
            json.dump(avtive, f, indent=4)
            print("[Success] users.json 寫入完成")


    def add(self, hostname, macaddress, days):
        self.macaddress = macaddress
        self.hostname = hostname
        self.days = int(days)

        check = 0
        newDevice = {
            "signup": self.timestamp,
            "days": self.days,
            "hostname": self.hostname,
            "macaddress": self.macaddress,
        }

        with codecs.open('users.json', 'r+', encoding='utf-8') as f:
            data = json.load(f)

            for i in range(len(data)):
                if data[i]["hostname"] == self.hostname:
                    print("[Error] hostname 已存在 !!")
                    check = 1

                if data[i]["macaddress"] == self.macaddress:
                    print("[Error] mac address 已存在 !!")
                    check = 1

            if check == 0:
                data.append(newDevice)
                f.seek(0)
                json.dump(data, f, indent=4)
                print("[Success] users.json 寫入完成")
            else:
                print("[Error] 資料錯誤，略過寫入 !!")
