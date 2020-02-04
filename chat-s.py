import socket
import time

HEADERSIZE = 60

'''
# Server Example 1
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print (f"Connection from {address} has been established!")
	clientsocket.send(bytes("Welcome to the chat server!", "utf-8"))
	clientsocket.close()
'''
'''
# Server Example 2
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print (f"Connection from {address} has been established!")
	msg = "Welcome to the Server!"
	msg = f'{len(msg):<{HEADERSIZE}}' + msg
	clientsocket.send(bytes(msg, "utf-8"))


	while True:
		time.sleep(5)
		msg = f"The time is: {time.asctime( time.localtime(time.time() ))}"
		msg = f'{len(msg):<{HEADERSIZE}}' + msg
		clientsocket.send(bytes(msg, "utf-8"))
'''




