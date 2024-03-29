import source.device.Cisco.device as device

class UserMode():
    def __init__(self, device):
        self.device = device
        self.device.connection.read()
        print(self.device.connection.read())

    def showVersion(self):
        self.device.connection.write('show version\n')
        print(self.device.connection.read())

    def showTime(self):
        self.device.connection.write('show clock\n')
        print(self.device.connection.read())