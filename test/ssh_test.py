import sys
sys.path.append(r'C:\网络文档\个人文件夹\陈一帆\python\NetCtrl')
import time
from source.user import User
from source.connection.ssh import SshConnection
import source.device.device as device
from source.device.Huawei import interfaceView as interfaceView

user1 = User('cisco','123')
connection1 = SshConnection(user1, '192.168.218.151')
ciscoSw = device.createDevice(connection1, device.Vendor.Cisco)
usermode = ciscoSw.userMode()
usermode.showTime()
usermode.showVersion()
ciscoSw.privilegeMode()
ciscoSw.globalConfigMode()


user2 = User('python','Admin@123')
connection2 = SshConnection(user2, '192.168.218.201')
HuaweiSw = device.createDevice(connection2, device.Vendor.Huawei)
userview = HuaweiSw.userView()
userview.showTime()
systemview = HuaweiSw.systemView()
intfaceview = HuaweiSw.interfaceView(interfaceView.Type.Gigabit, 1)

