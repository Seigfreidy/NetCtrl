from enum import Enum
from user import User

class Connection:
    def __init__(self, user, destinationIp):
        self.user = user
        self.destinationIp = destinationIp