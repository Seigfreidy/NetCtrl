import sys
sys.path.append(r'D:\Git\NetCtrl')
import device.Cisco.device as device
import globalconfig

class Firewall(device.Device):
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