import time

class PrivilegeMode():
    def __init__(self, device):
        self.device = device
    
    def setEcholines(self, num = 0):
        self.device.connection.write('terminal length ' + str(num) + ' \n')
        print(self.device.connection.read())
    
    def currentConfiguration(self):
        self.device.connection.read()
        self.device.connection.write('show running-config\n')
        time.sleep(5)
        return self.device.connection.read()
    
    def snmpInfo(self):
        self.device.connection.read()
        self.device.connection.write('show running-config | include snmp\n')
        time.sleep(0.5)
        return self.device.connection.read()