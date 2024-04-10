import sys
sys.path.append(r'D:\Git')

from NetCtrl.source.user import User
from NetCtrl.source.connection.ssh import SshConnection
import NetCtrl.source.device.Cisco.device as device
import NetCtrl.source.echoOperation.basic as operation

user = User('chenyf','chenyf@123')
connection = SshConnection(user, '192.168.218.141')
XscloudtestFw = device.createDevice(connection, device.Type.Firewall, device.Model.Firepower)
privilegemode = XscloudtestFw.privilegeMode('chenyf')
privilegemode.setEcholines()
config = privilegemode.currentConfiguration()

operation.show(config)
operation.log(config, r'log\xscloudtest_fw_log.txt')