import sys
sys.path.append(r'D:\Git\NetCtrl\source')
from user import User
from device import Device
from ssh import SshConnection
# import device as device
# import ssh as ssh


device1 = Device('192.168.218.151')
user1 = User('cisco','123')

connection2 = SshConnection(user1, device1)
connection2.connect()
print(connection2.status)