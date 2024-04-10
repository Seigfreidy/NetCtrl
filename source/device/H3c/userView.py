import source.device.Huawei.device as device

class UserView():
    def __init__(self, device):
        self.device = device
        self.device.connection.read()
        print(self.device.connection.read())

    def setEchoLines(self, num = 0):
        self.device.connection.write('screen-length ' + str(num) + ' temporary\n')

    def version(self):
        self.device.connection.write('display version\n')
        return self.device.connection.read()

    def time(self):
        self.device.connection.write('display clock\n')
        return self.device.connection.read()

    def currentConfiguration(self):
        self.device.connection.write('display current-configuration\n')
        return self.device.connection.read()