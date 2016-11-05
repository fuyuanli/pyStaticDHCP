#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

class ipRange:
    def __init__(self, args):
        try:
            if args == "from"  or args == "to":
                with open('subnet.json') as subnetJson:
                    subnet = json.load(subnetJson)

                    ip = subnet[0]["range"][args]
                    dot1 = ip.find(".")
                    dot2 = ip.find(".", dot1 + 1)
                    dot3 = ip.find(".", dot2 + 1)

                    self.ip = subnet[0]["range"][args]
                    self.getB = int(ip[dot2+1:dot3])
                    self.getC = int(ip[dot3+1:])

            else:
                print("參數錯誤")
        except:
            print("發生錯誤")

class Generate:
    def __init__(self):
        with open('subnet.json') as subnetJson:
            self.subnet = json.load(subnetJson)

        self.routhers = self.subnet[0]["routhers"]
        self.broadcastAddress = self.subnet[0]["broadcast-address"]

        with open('users.json') as usersJson:
            self.users = json.load(usersJson)
        self.ipTo = ipRange("to")
        self.ipFrom = ipRange("from")

    def checkExist(self, ipList, ip):
        listNums = len(ipList)
        for i in range(listNums):
            if ipList[i] == ip:
                ipList.remove(ip)
                print("[checkExist]", ip, "已存在，從陣列移除。")
                break

    def allIPs(self, theNum):


        if theNum == 0:
            ips = self.ipTo.getC - self.ipFrom.getC

        if theNum == 1:
            ips = (254 - self.ipFrom.getC) + self.ipTo.getC

        if theNum >= 2:
            ips = 254 * (theNum - 1) + (255 - self.ipFrom.getC) + self.ipTo.getC
        return ips

    def ipLoop(self, x, y, i):
        saver = ""
        b = self.ipFrom
        ipHead = b.ip[:len(b.ip)-len(str(b.getB)+"."+str(b.getC))]
        for j in range(x, y):
            saver += ipHead + str(self.ipFrom.getB+i) + "." +str(j+1) + "\n"
        return saver

    def list(self):
        fromB = self.ipFrom.getB
        toB = self.ipTo.getB
        fromC = self.ipFrom.getC
        toC = self.ipTo.getC

        bRange = int(toB - fromB) # example : 10.1.10.1 - 10.1.2.1 , 10-2=8
        ips = self.allIPs(bRange)
        classBNum = int(ips/254)

        theStatic = ""

        for i in range(classBNum +1):
            if classBNum == 0:
                theStatic += self.ipLoop(fromC, toC, i, theStatic)
            if classBNum > 0:
                if i != classBNum:
                    if i == 0 :
                        theStatic += self.ipLoop(fromC-1, 254, i)
                    if i != 0 :
                        theStatic += self.ipLoop(0, 254, i)
                if i == classBNum:
                    theStatic += self.ipLoop(0, toC, i)
        ipList = theStatic.split("\n")
        self.checkExist(ipList, self.routhers)
        self.checkExist(ipList, self.broadcastAddress)
        return ipList


        #subnet += "\thost %s { hardware ethernet %s; fixed-address %s} \n" % (usersList[i]["hostname"], usersList[i]["macaddress"], usersList[i]["static"])
