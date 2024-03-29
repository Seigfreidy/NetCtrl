from enum import Enum
import sys
sys.path.append(r'D:\Git\NetCtrl')
import source.Huawei.userView as userView
import source.Huawei.systemView as systemView


class View(Enum):
    Unknow = 0
    User = 1
    System = 2
    Interface = 3
    Protocol = 4

class Device:
    def __init__(self, connection):
        self.connection = connection
        self.__view__ = View.Unknow

    def userView(self):
        if self.__view__ == View.Unknow:
            self.connection.connect()
            self.connection.write('n\n')
        elif self.__view__ == View.User:
            pass
        elif self.__view__ == View.System:
            self.__quit2UpLevelView__()
        elif self.__view__ == View.Interface:
            self.__quit2UpLevelView__()
            self.__quit2UpLevelView__()
        self.__view__ = View.User
        return userView.UserView(self)

    def systemView(self):
        if self.__view__ == View.Unknow:
            self.connection.connect()
            self.connection.write('n\n')
        elif self.__view__ == View.User:
            self.__enterSystemView__()
        elif self.__view__ == View.System:
            pass
        elif self.__view__ == View.Interface:
            self.__quit2UpLevelView__()
        self.__view__ = View.System
        return systemView.systemView(self)

    def __quit2UserView__(self):
        pass

    def __quit2UpLevelView__(self):
        self.connection.write('quit\n')

    def __enterSystemView__(self):
        self.connection.write('system-view\n')
    # def login(self):
    #     self.connection.connect()
    #     self.connection.write('n\n')
    #     print(self.connection.read())
    
    # def logout(self):
    #     self.connection.disconnect()

    # def displayMode(self):
    #     return display.DisplayMode(self)

    # def configInterface(self):
    #     self.connection.write('system-view\n')
    #     print(self.connection.read())
    #     return config.ConfigInterface(self)