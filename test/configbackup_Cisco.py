import sys
sys.path.append(r'D:\Git')

from NetCtrl.source.user import User
from NetCtrl.source.connection.ssh import SshConnection
import NetCtrl.source.device.Cisco.device as device
import NetCtrl.source.echoOperation.basic as operation

user = User('cisco','123')
connection = SshConnection(user, '192.168.218.141')
CiscoSw = device.createDevice(connection, device.Type.Switch)
privilegemode = CiscoSw.privilegeMode('123')
privilegemode.setEcholines()
globalconfigmode = CiscoSw.globalConfigMode()


# config = privilegemode.currentConfiguration()

# operation.show(config)
# operation.log(config, r'log\Cisco_Sw_log.txt')
config = globalconfigmode.scriptConifig(r'script\hostnamechange.txt')

