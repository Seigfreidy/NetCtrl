from enum import Enum
import operation

class Content(Enum):
    Time = 0
    Version = 1
    All = 2

class Display(operation.Operation):
    def __init__(self, content, type, device):
        super().__init__(type, device)
        self.content = content
        self.devtype = device.type
        self.vendor = device.vendor