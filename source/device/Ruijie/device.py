from enum import Enum
import sys
sys.path.append(r'D:\Git\NetCtrl')
import source.device.Cisco.user as user
import source.device.Cisco.privilege as privilege
import source.device.Cisco.globalconfig as globalconfig

class Mode(Enum):
    Unknow = 0
    User = 1
    Privilege = 2
    GlobalConfig = 3

class Device:
    def __init__(self, connection):
        self.connection = connection
        self.__mode__ = Mode.Unknow

    def userMode(self):
        if self.__mode__ == Mode.Unknow:
            self.connection.connect()
        elif self.__mode__ == Mode.User:
            pass
        elif self.__mode__ == Mode.Privilege:
            self.__quitCurrentMode__()
        elif self.__mode__ == Mode.GlobalConfig:
            self.__quitCurrentMode__()
            self.__quitCurrentMode__()
        self.__mode__ = Mode.User
        return user.UserMode(self)

    def privilegeMode(self, password):
        if self.__mode__ == Mode.Unknow:
            self.connection.connect()
            self.__enterPrivilege__(password)
        elif self.__mode__ == Mode.User:
            self.__enterPrivilege__(password)
        elif self.__mode__ == Mode.Privilege:
            pass
        elif self.__mode__ == Mode.GlobalConfig:
            self.__quitCurrentMode__(password)
        self.__mode__ = Mode.Privilege
        return privilege.PrivilegeMode(self)

    def globalConfigMode(self):
        if self.__mode__ == Mode.Unknow:
            self.connection.connect()
            self.__enterPrivilege__()
            self.__enterConfig__()
        elif self.__mode__ == Mode.User:
            self.__enterPrivilege__()
            self.__enterConfig__()
        elif self.__mode__ == Mode.Privilege:
            self.__enterConfig__()
        elif self.__mode__ == Mode.GlobalConfig:
            pass
        self.__mode__ = Mode.GlobalConfig
        return globalconfig.GlobalConfigMode(self)

    def __quitCurrentMode__(self):
        self.connection.write('quit\n')
    
    def __enterPrivilege__(self, password):
        self.connection.write('enable\n')
        self.connection.write(password +'\n')

    def __enterConfig__(self):
        self.connection.write('configure terminal\n')
