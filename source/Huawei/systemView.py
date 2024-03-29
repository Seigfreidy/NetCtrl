import device

class systemView():
    def __init__(self, device):
        self.device = device
        # self.device.connection.read()
        print(self.device.connection.read())
    
    def xx(self):
        print(self.device.connection.read())
