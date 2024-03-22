class Administor:
    def __init__(self, id):
        self.id = id
        self.username = ''
        self.password = ''
    
    def createUser(self, username, password):
        self.username = username
        self.password = password