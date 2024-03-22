# from typing import Any, SupportsIndex
import connection
import time
import paramiko

class SshConnection(connection.Connection):
    def __init__(self, user, dev, port = 22, timeover = 10):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        super().__init__(user, dev)
        self.host = dev.manageIp
        self.port = port
        self.username = user.username
        self.password = user.password
        self.timeover = timeover
        self.codetype = "utf-8"

    
    def __exit__(self):
        self.ssh_client.close()
        self.status = connection.connectionStatus.Disconnected

    def connect(self):
        self.ssh_client.connect(hostname=self.host,username=self.username,password=self.password,look_for_keys=False)
        print("Successfully login!\n")
        self.status = connection.connectionStatus.Connected
        self.channel = self.ssh_client.invoke_shell(width = 10000, height = 10000)
    
    def write(self, text):
        self.channel.send(text.encode(self.codetype))
    
    def read(self):
        data = b""
        while self.channel.recv_ready():
            data += self.channel.recv(1024)
            time.sleep(0.1)
        text = data.decode(self.codetype, "backslashreplace")
        return text
        