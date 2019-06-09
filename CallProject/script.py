import socket
from time import sleep

ami_cmd1 = '''Action: login
Events: off
Username: mark
Secret: mysecret\n\n'''

ami_cmd2 = '''Action: Originate
Channel: SIP/1001
Context: outcoling
Exten: 1002
Priority: 1
Callerid: 1001
Timeout: 30000\n\n'''

def ConnectToAsterisk(number=None):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = '51.140.244.177'
    PORT = 5038

    s.connect((HOST, PORT))
    s.send(bytes(ami_cmd1, 'utf-8'))
    sleep(0.1)
    data = s.recv(1024)

    calldata = ami_cmd2
    print(calldata)
    s.send(bytes(calldata, 'utf-8'))
    sleep(0.1)
    data = s.recv(1024)
    print(data)
    s.close()

ConnectToAsterisk(number="1002")

