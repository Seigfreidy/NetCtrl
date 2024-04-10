import sys
sys.path.append(r'D:\Git\NetCtrl')
import  source.device.Huawei.device as device
from source.device.Huawei.device import Device


class FW_2(Device):
    def __init__(self, connection):
        super().__init__(connection)
    
    def userView(self):
        if self.__view__ == device.View.Unknow:
            self.connection.connect()
        elif self.__view__ == device.View.User:
            pass
        elif self.__view__ == device.View.System:
            self.__quit2UpLevelView__()
        elif self.__view__ == device.View.Interface:
            self.__quit2UpLevelView__()
            self.__quit2UpLevelView__()
        self.__view__ = device.View.User
        return device.userView.UserView(self)