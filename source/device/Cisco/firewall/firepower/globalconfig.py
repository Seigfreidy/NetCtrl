import NetCtrl.source.device.Cisco.globalconfig as globalConfigMode

class GlobalConfigMode(globalConfigMode.GlobalConfigMode):
    def __init__(self, device):
        super().__init__(device)