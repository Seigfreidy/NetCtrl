import sys
sys.path.append(r'D:\Git\NetCtrl')

from source.user import User
from source.connection.ssh import SshConnection
import source.device.Cisco.device as device
import source.echoOperation.basic as operation

user = User('cisco','123')
connection = SshConnection(user, '192.168.218.141')
CiscoSw = device.createDevice(connection, device.Type.Switch)
privilegemode = CiscoSw.privilegeMode('123')
privilegemode.setEcholines()
config = privilegemode.currentConfiguration()

operation.show(config)
operation.log(config, r'log\Cisco_Sw_log.txt')

