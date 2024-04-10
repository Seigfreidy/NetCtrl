import sys
sys.path.append(r'D:\Git')

from NetCtrl.source.user import User
from NetCtrl.source.connection.ssh import SshConnection
import NetCtrl.source.device.Huawei.device as device
import NetCtrl.source.echoOperation.basic as operation

# user = User('huawei','Admin@123')
user = User()
user.loginInfoInput()
connection = SshConnection(user, '192.168.218.151')
HuaweiSw = device.createDevice(connection, device.Type.Switch)
userview = HuaweiSw.userView()

operation.show(userview.time())

