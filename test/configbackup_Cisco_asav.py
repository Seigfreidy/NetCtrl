import sys
sys.path.append(r'D:\Git')

import NetCtrl.source.device.Cisco.device as device
from NetCtrl.source.user import User
from NetCtrl.source.connection.ssh import SshConnection
import NetCtrl.source.echoOperation.basic as operation

user = User('cisco','123')
connection = SshConnection(user, '192.168.218.145')
Asav = device.createDevice(connection, device.Type.Firewall, device.Model.ASAV)
privilegemode = Asav.privilegeMode('123')
privilegemode = Asav.privilegeMode()
privilegemode.setEcholines()
config = privilegemode.currentConfiguration()

operation.show(config)
operation.log(config, r'log\Cisco_Asav_log.txt')

