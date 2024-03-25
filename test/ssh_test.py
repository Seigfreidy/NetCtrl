import sys
sys.path.append(r'D:\Git\NetCtrl\source')
from user import User
from device import Device
from ssh import SshConnection
import Cisco.showTime

user1 = User('cisco','123')

connection2 = SshConnection(user1, '192.168.218.151')
CiscoFw = Device(connection2, Device)
# connection2.connect()
print(connection2.status)