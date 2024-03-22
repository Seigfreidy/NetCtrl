from enum import Enum
import admin
import device

class connectionStatus(Enum):
    Connected = 1
    Disconnected = 0

class Connection:
    def __init__(self):
        self.user = ''
        self.dev = ''
        self.status = connectionStatus.Disconnected
        pass

    def create(self, user, dev):
        self.user = user
        self.dev = dev
        if self.user and self.dev:
            self.status = connectionStatus.Connected
            return self
        else:
            return False