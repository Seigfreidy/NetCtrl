# import sys
# sys.path.append(r'D:\Git\NetCtrl\source')
from user import User
from ssh import SshConnection
import Cisco.device
import device

user1 = User('cisco','123')

connection = SshConnection(user1, '192.168.218.151')
ciscoFw = device.createDevice(connection, device.Vendor.Cisco)
# CiscoFw = device.Device(connection2, device.Type.Firewall, device.Vendor.Cisco)
# CiscoFw.connection.connect()
# connection2.connect()
print(connection.status)