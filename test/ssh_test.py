import sys
sys.path.append(r'C:\网络文档\个人文件夹\陈一帆\python\NetCtrl')
import time
from source.user import User
from source.connection.ssh import SshConnection
import source.device.device as device
from source.device.Huawei import interfaceView as interfaceView

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

