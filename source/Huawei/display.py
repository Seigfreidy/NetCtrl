import device

class DisplayInterface():
    def __init__(self, device):
        self.device = device
    
    def setEchoLines(self, num = 0):
        command = 'screen-length ' + str(num) +' temporary \n'
        self.device.connection.write(command)
    
    def showTime(self):
        self.device.connection.write('display clock\n')
        print(self.device.connection.read())
    
    def showAllConfig(self):
        self.device.connection.write('display current-configuration\n')
        print(self.device.connection.read())