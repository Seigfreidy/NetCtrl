from enum import Enum

class Mode(Enum):
    Unknow = 0
    Basic = 1
    Config = 2

class Device:
    def __init__(self, connection):
        self.connection = connection
        self.mode = Mode.Unknow

    def login(self):
        self.connection.connect()
        # print('successfully login to a Huawei device')
        self.connection.write('n\n')
        self.mode = Mode.Basic
        print(self.connection.read())
    
    def logout(self):
        self.connection.disconnect()
        self.mode = Mode.Unknow

    def enterConfigMode(self):
        if self.mode == Mode.Basic:
            self.connection.write('system-view\n')
            self.mode = Mode.Config
            print(self.connection.read())
        else:
            print('It is not at basic mode')

    def showTime(self):
        self.connection.write('display clock\n')
        print(self.connection.read())