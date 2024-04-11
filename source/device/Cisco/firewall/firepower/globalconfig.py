# import sys
<<<<<<< HEAD
# sys.path.append(r'C:\网络文档\个人文件夹\陈一帆\python\NetCtrl')
=======
# sys.path.append(r'D:\Git\NetCtrl')
>>>>>>> fa0d7b3555bca013cfca202f03026df87afc93f1
import NetCtrl.source.device.Cisco.globalconfig as globalConfigMode

class GlobalConfigMode(globalConfigMode.GlobalConfigMode):
    def __init__(self, device):
        super().__init__(device)