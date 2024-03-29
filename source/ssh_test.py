# import sys
# sys.path.append(r'D:\Git\NetCtrl')
import time
from user import User
from ssh import SshConnection
# import Cisco
# import Huawei
import device

# user1 = User('cisco','123')
# connection1 = SshConnection(user1, '192.168.218.151')
# ciscoSw = device.createDevice(connection1, device.Vendor.Cisco)
# # ciscoSw.showTime()
# usermode = ciscoSw.userMode()
# usermode.showTime()
# usermode.showVersion()

# ciscoSw.privilegeMode()
# ciscoSw.globalConfigMode()




user2 = User('python','Admin@123')
connection2 = SshConnection(user2, '192.168.218.201')
HuaweiSw = device.createDevice(connection2, device.Vendor.Huawei)
userview = HuaweiSw.userView()
userview.showTime()
systemview = HuaweiSw.systemView()
