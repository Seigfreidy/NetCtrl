from enum import Enum
from connection import Connection

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

def createDevice(connection, vendor):
    if vendor == Vendor.Cisco:
        from .Cisco import device
        return device.Device(connection)