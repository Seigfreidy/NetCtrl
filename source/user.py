import getpass

class User:
    def __init__(self, username = '', password = ''):
        self.username = username
        self.password = password
    # def __init__(self):
    #     pass

    def loginInfoInput(self):
        self.username = input("input the username: ")
        print("the username: ", self.username)
        self.password = getpass.getpass("input the password: ")
        print("the password: ", self.password)