import os  
import shutil  
  
def delete_pycache_folders(root_dir):  
    for dirpath, dirnames, filenames in os.walk(root_dir):  
        if "__pycache__" in dirnames:  
            shutil.rmtree(os.path.join(dirpath, "__pycache__"))  

root_dir = r'D:\Git\NetCtrl'
delete_pycache_folders(root_dir)