# import sys
<<<<<<< HEAD
# sys.path.append(r'C:\网络文档\个人文件夹\陈一帆\python\NetCtrl')
=======
# sys.path.append(r'D:\Git\NetCtrl')
>>>>>>> fa0d7b3555bca013cfca202f03026df87afc93f1
import NetCtrl.source.device.Cisco.device as device
import NetCtrl.source.device.Cisco.firewall.firepower.globalconfig as globalconfig
import NetCtrl.source.device.Cisco.firewall.firepower.privilege as privilege

class Firepower(device.Device):
    def __init__(self, connection):
        super().__init__(connection)
    
    def globalConfigMode(self):
        if self.__mode__ == device.Mode.Unknow:
            self.connection.connect()
            self.__enterPrivilege__()
            self.__enterConfig__()
        elif self.__mode__ == device.Mode.User:
            self.__enterPrivilege__()
            self.__enterConfig__()
        elif self.__mode__ == device.Mode.Privilege:
            self.__enterConfig__()
        elif self.__mode__ == device.Mode.GlobalConfig:
            pass
        self.__mode__ = device.Mode.GlobalConfig
        return globalconfig.GlobalConfigMode(self)

    def privilegeMode(self, password = ''):
        if self.__mode__ == device.Mode.Unknow:
            self.connection.connect()
            self.__enterPrivilege__(password)
        elif self.__mode__ == device.Mode.User:
            self.__enterPrivilege__(password)
        elif self.__mode__ == device.Mode.Privilege:
            pass
        elif self.__mode__ == device.Mode.GlobalConfig:
            self.__quitCurrentMode__(password)
        self.__mode__ = device.Mode.Privilege
        return privilege.PrivilegeMode(self)