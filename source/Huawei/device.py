from enum import Enum
import Huawei.display as display
import Huawei.config as config

class Device:
    def __init__(self, connection):
        self.connection = connection

    def login(self):
        self.connection.connect()
        self.connection.write('n\n')
        print(self.connection.read())
    
    def logout(self):
        self.connection.disconnect()

    def displayInterface(self):
        return display.DisplayInterface(self)

    def configInterface(self):
        self.connection.write('system-view\n')
        print(self.connection.read())
        return config.ConfigInterface(self)