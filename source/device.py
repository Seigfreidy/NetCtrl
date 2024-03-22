from enum import Enum

class Type(Enum):
    Unknow = 0
    Switch = 1
    Router = 2
    Firewall = 3

class Vendor(Enum):
    Unknow = 0
    Huawei = 1
    Cisco = 2
    H3c = 3
    Reijie = 4

class Device:
    def __init__(self, manageIp, type = Type.Unknow, vendor = Vendor.Unknow):
        self.type = type
        self.vendor = vendor
        self.manageIp = manageIp

