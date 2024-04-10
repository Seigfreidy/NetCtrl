# from enum import Enum
# import sys
# sys.path.append(r'D:\Git\NetCtrl')
# from connection import Connection

# class Type(Enum):
#     Unknow = 0
#     Switch = 1
#     Router = 2
#     Firewall = 3

# class Vendor(Enum):
#     Unknow = 0
#     Huawei = 1
#     Cisco = 2
#     H3c = 3
#     Ruijie = 4

# def createDevice(connection, vendor, type = Type.Unknow):
#     if vendor == Vendor.Cisco:
#         if type == Type.Firewall:
#             from source.device.Cisco.firewall import Firewall
#             return Firewall.Firewall(connection)
#         else:
#             from source.device.Cisco import device
#             return Firewall.Device(connection)
#     if vendor == Vendor.Huawei:
#         if type == Type.Firewall:
#             from source.device.Huawei.firewall.fw_2 import fw_2
#             return fw_2.FW_2
#         from source.device.Huawei import device
#         return Firewall.Device(connection)
#     if vendor == Vendor.Ruijie:
#         if type == Type.Firewall:
#             from source.device.Ruijie.firewall import device
#             return Firewall.Firewall(connection)
#         else:
#             from source.device.Ruijie import device
#             return Firewall.Device(connection)
#     if vendor == Vendor.H3c:
#         # if type == Type.Firewall:
#         #     from source.device.Huawei.firewall.fw_2 import fw_2
#         #     return fw_2.FW_2
#         from source.device.H3c import device
#         return Firewall.Device(connection)