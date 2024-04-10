import NetCtrl.source.device.Cisco.privilege as privilege

class PrivilegeMode(privilege.PrivilegeMode):
    def __init__(self, device):
        super().__init__(device)
    
    def setEcholines(self, num = 0):
        self.device.connection.write('terminal pager ' + str(num) + ' \n')
        print(self.device.connection.read())
    
    # def currentConfiguration(self):
    #     self.device.connection.write('show running-config\n')
    #     time.sleep(5)
    #     return self.device.connection.read()