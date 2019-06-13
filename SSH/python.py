import socket

def sendFun(sendData):
	sock = socket.socket()
	sock.connect((10.0.41.226, 9090))
	sock.send(sendData)

	data = sock.recv(1024)
	sock.close()

	print(data)
	print("OK")

buffer=""
f = open('/var/log/messages', 'r')
for line in f.readlines():
	print line
	if 'Accepted password' in line:
		buffer=buffer+line+"\n"
	elif 'Accepted publickey' in line:
		buffer=buffer+line+"\n"
f.close()
sendFun(buffer)