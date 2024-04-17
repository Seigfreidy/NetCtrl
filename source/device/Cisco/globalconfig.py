class GlobalConfigMode():
    def __init__(self, device):
        self.device = device

    def scriptConifig(self, path):
        try:  
            with open(path, 'r') as file:  
                data = file.read()
                self.device.connection.write(data)
                print(self.device.connection.read())
        except FileNotFoundError:  
            print("cannot find the script.\n")