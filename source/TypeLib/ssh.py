import connection
import paramiko

class SshConnection(connection.Connection):
    def __init__(self):
        super().__init__()

    def create(self, user, dev):
        self.user = user
        self.dev = dev
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=dev.manageIp,username=user.username,password=user.password,look_for_keys=False)
        print("Successfully login!\n")
        