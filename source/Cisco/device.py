from enum import Enum

class Mode(Enum):
    Unknow = 0
    Basic = 1
    User = 2
    Config = 3

class Device:
    def __init__(self, connection):
        self.connection = connection

    def logout(self):
        self.connection.disconnect()

    def login(self):
        self.connection.connect()
        print('successfully login to a Cisco device')
        print(self.connection.read())

    def enterUserMode(self):
        self.connection.write('enable\n')
        self.connection.write('123\n')
        print(self.connection.read())

    def showVersion(self):
        self.connection.write('show version\n')
        print(self.connection.read())

    def showTime(self):
        self.connection.write('show clock\n')
        print(self.connection.read())
    
    def showAllConfig(self):
        self.connection.write('show running-config\n')
        print(self.connection.read())       