from enum import Enum
from device import Device
from user import User

class connectionStatus(Enum):
    Connected = 1
    Disconnected = 0

class Connection:
    def __init__(self, user, dev):
        self.user = user
        self.device = dev
        self.status = connectionStatus.Disconnected