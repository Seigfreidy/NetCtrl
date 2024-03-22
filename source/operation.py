from enum import Enum

class type(Enum):
    Display = 0
    Config = 1

class Operation:
    def __init__(self, type, device):
        self.type = type
        self.device = device