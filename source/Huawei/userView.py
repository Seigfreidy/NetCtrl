import device

class UserView():
    def __init__(self, device):
        self.device = device
        self.device.connection.read()
        print(self.device.connection.read())

    def showVersion(self):
        self.device.connection.write('display version\n')
        print(self.device.connection.read())

    def showTime(self):
        self.device.connection.write('display clock\n')
        print(self.device.connection.read())