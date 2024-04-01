import sys
sys.path.append(r'D:\Git\NetCtrl')
from source.device.Huawei.device import Device

class Switch(Device):
    def __init__(self, connection):
        super().__init__(connection)
