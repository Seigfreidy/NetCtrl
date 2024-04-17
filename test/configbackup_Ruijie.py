import sys
sys.path.append(r'C:\网络文档\个人文件夹\陈一帆\python')

from NetCtrl.source.user import User
from NetCtrl.source.connection.ssh import SshConnection
import NetCtrl.source.device.Ruijie.device as device
import NetCtrl.source.operation.fileOP as operation


# operation.show(snmpinfo)
# print(snmpinfo)
# print(operation.match(snmpinfo, 'no enable service snmp-agent'))
# if operation.match(snmpinfo, 'no enable service snmp-agent'):
#     print('enable service.\n')

excel = operation.read_file(r'script\ips.xlsx')
for index, row in excel.iterrows():  
    # 访问每一行的数据
    ip = row['IP']
    username = row['username']  
    password = row['password']  
    enablepass = row['enablepass']

    user = User(username,password)
    connection = SshConnection(user, ip)
    RuijieSw = device.createDevice(connection, device.Type.Switch)
    privilegemode = RuijieSw.privilegeMode(enablepass)
    privilegemode.setEcholines()
    config = privilegemode.currentConfiguration()
    filename = 'log\Ruijie\\' + str(ip) + '.txt'
    operation.log(config, filename)

