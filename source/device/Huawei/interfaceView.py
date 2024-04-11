from enum import Enum
import NetCtrl.source.device.Huawei.device as device

class Type(Enum):
    Gigabit = 'GE'
    Ten_Gigabit = 1
    Hundred_Gigabit = 2
    Aggregation = 3


class InterfaceView():
    def __init__(self, device, type, num):
        self.device = device
        self.type = type
        self.num = num
        # self.device.connection.read()
        print(self.device.connection.read())

