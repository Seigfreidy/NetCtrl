import sys
sys.path.append(r'D:\Git\NetCtrl')

from source.user import User
from source.connection.ssh import SshConnection
import source.device.device as device

user2 = User('python','Admin@123')
connection2 = SshConnection(user2, '192.168.218.201')
HuaweiSw = device.createDevice(connection2, device.Vendor.Huawei)
userview = HuaweiSw.userView()

