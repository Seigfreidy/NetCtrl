from enum import Enum
from user import User

# class connectionStatus(Enum):
#     Connected = 1
#     Disconnected = 0

class Connection:
    def __init__(self, user, destinationIp):
        self.user = user
        self.destinationIp = destinationIp
        # self.status = connectionStatus.Disconnected