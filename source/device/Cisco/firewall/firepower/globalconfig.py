# import sys
# sys.path.append(r'C:\网络文档\个人文件夹\陈一帆\python\NetCtrl')
import NetCtrl.source.device.Cisco.globalconfig as globalConfigMode

class GlobalConfigMode(globalConfigMode.GlobalConfigMode):
    def __init__(self, device):
        super().__init__(device)