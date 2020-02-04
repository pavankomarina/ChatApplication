import socket

HEADERSIZE = 60

'''
# Client Example 1
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

full_msg = ""
while True:
	msg = s.recv(48)
	if len(msg) <=0:
		break
	full_msg += msg.decode("utf-8")

print(full_msg)

'''
'''
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
	
	full_msg = ""
	new_msg = True
	while True:
		msg = s.recv(76)
		if new_msg:
			print(f"new message length: {msg[:HEADERSIZE]}")
			msglen = int(msg[:HEADERSIZE])
			new_msg = False

		full_msg += msg.decode("utf-8")

		if len(full_msg)-HEADERSIZE == msglen:
			print("Full Message Received")
			print(full_msg[HEADERSIZE:])
			new_msg = True
			full_msg = ''

	print(full_msg)
'''	