import sys
sys.path.append(r'D:\Git\NetCtrl')

from source.user import User
from source.connection.ssh import SshConnection
import source.device.device as device
import source.echoOperation.basic as operation

user = User('python','Admin@123')
connection = SshConnection(user, '192.168.218.201')
HuaweiSw = device.createDevice(connection, device.Vendor.Huawei)
userview = HuaweiSw.userView()
userview.setEchoLines()
config = userview.currentConfiguration()
operation.show(config)
operation.log(config, r'log\huaweilog.txt')

