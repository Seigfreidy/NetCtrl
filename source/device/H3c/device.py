from enum import Enum
import sys
sys.path.append(r'C:\网络文档\个人文件夹\陈一帆\python\NetCtrl')
import source.device.Huawei.userView as userView
import source.device.Huawei.systemView as systemView
import source.device.Huawei.interfaceView as interfaceView


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
        return systemView.SystemView(self)

    def interfaceView(self, type, num):
        if self.__view__ == View.Unknow:
            self.connection.connect()
            self.connection.write('n\n')
        elif self.__view__ == View.User:
            self.__enterSystemView__()
        elif self.__view__ == View.System:
            self.__enterIfView__(type, num)
        elif self.__view__ == View.Interface:
            pass
        self.__view__ = View.Interface
        return interfaceView.InterfaceView(self, type, num)

    def __quit2UserView__(self):
        pass

    def __quit2UpLevelView__(self):
        self.connection.write('quit\n')

    def __enterSystemView__(self):
        self.connection.write('system-view\n')

    def __enterIfView__(self, type, num):
        command = 'interface '
        command += type.value + ' 1/0/' + str(num)
        self.connection.write(command +'\n')
