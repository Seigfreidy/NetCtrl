from enum import Enum
import sys
sys.path.append(r'D:\Git\NetCtrl')
# from connection import Connection

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

def createDevice(connection, vendor, type = Type.Unknow):
    if vendor == Vendor.Cisco:
        from source.device.Cisco import device
        return device.Device(connection)
    if vendor == Vendor.Huawei:
        from source.device.Huawei import device
        return device.Device(connection)