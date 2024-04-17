import os  
import shutil  
  
def delete_pycache_folders(root_dir):  
    for dirpath, dirnames, filenames in os.walk(root_dir):  
        if "__pycache__" in dirnames:  
            shutil.rmtree(os.path.join(dirpath, "__pycache__"))  
  
# 使用你的项目根目录替换下面的路径  
root_dir = r'D:\Git\NetCtrl'
delete_pycache_folders(root_dir)