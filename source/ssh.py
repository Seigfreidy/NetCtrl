# from typing import Any, SupportsIndex
import connection
import time
import paramiko

class SshConnection(connection.Connection):
    def __init__(self, user, destinationIp, port = 22, timeover = 10):
        super().__init__(user, destinationIp)
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.host = destinationIp
        self.port = port
        self.username = user.username
        self.password = user.password
        self.timeover = timeover
        self.codetype = "utf-8"

    
    def disconnect(self):
        self.ssh_client.close()

    def connect(self):
        self.ssh_client.connect(hostname=self.host,username=self.username,password=self.password,look_for_keys=False)
        print("Successfully login!\n")
        self.channel = self.ssh_client.invoke_shell(width = 10000, height = 10000)
    
    def write(self, text):
        self.channel.send(text.encode(self.codetype))
        time.sleep(0.2)
    
    def read(self):
        data = b""
        while self.channel.recv_ready():
            data += self.channel.recv(2048)
            time.sleep(0.1)
        text = data.decode(self.codetype)
        return text
        