# import sys
# sys.path.append(r'D:\Git\NetCtrl\source')
import time
from user import User
from ssh import SshConnection
# import Cisco
# import Huawei
import device

# user1 = User('cisco','123')
# connection1 = SshConnection(user1, '192.168.218.151')
# ciscoSw = device.createDevice(connection1, device.Vendor.Cisco)
# ciscoSw.login()
# ciscoSw.showTime()
# ciscoSw.enterUserMode()
# ciscoSw.showAllConfig()
# ciscoSw.logout()


user2 = User('python','Admin@123')
connection2 = SshConnection(user2, '192.168.218.201')
HuaweiSw = device.createDevice(connection2, device.Vendor.Huawei)
HuaweiSw.login()
DispIf = HuaweiSw.displayInterface()
DispIf.setEchoLines()
DispIf.showAllConfig()
# DisIf.showTime()

