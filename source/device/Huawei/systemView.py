import source.device.Huawei.device as device

class SystemView():
    def __init__(self, device):
        self.device = device
        # self.device.connection.read()
        print(self.device.connection.read())
    
    def xx(self):
        print(self.device.connection.read())
