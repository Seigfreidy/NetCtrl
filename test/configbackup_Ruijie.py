import sys
sys.path.append(r'D:\Git\NetCtrl')

from source.user import User
from source.connection.ssh import SshConnection
import source.device.device as device
import source.echoOperation.basic as operation

user = User('reijie','123')
# user = User()
# user.loginInfoInput()
connection = SshConnection(user, '192.168.218.161')
CiscoSw = device.createDevice(connection, device.Vendor.Ruijie)
privilegemode = CiscoSw.privilegeMode('')
privilegemode.setEcholines()
config = privilegemode.currentConfiguration()

operation.show(config)
operation.log(config, r'log\Ruijielog.txt')

