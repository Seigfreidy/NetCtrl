import pandas as pd

def log(text, path):
    fileout = open(path, "w+")
    fileout.write(text)
    fileout.close()

def read_file(path):
    return pd.read_excel(path, dtype = str)