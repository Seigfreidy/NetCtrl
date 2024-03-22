import sys
sys.path.append(r'D:\Git\NetCtrl\source\TypeLib')
import TypeLib.admin as admin
import TypeLib.device as device
import TypeLib.connection as connection
import TypeLib.ssh as ssh

admin1 = admin.Administor(1)
device1 = device.Device(0)

connection1 = connection.Connection()
print(connection1.status)

connection1.create(admin1, device1)
print(connection1.status)

connection2 = ssh.SshConnection()
connection2.create(admin1, device1)
print(connection2.status)