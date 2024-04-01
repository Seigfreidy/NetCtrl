def show(text):
    print(text)

def log(text, path):
    fileout = open(path, "w+")
    fileout.write(text)
    fileout.close()
    