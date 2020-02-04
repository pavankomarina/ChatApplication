import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target = input("What IP Address to scan:")

def pscan(port):

	try:
		connect = s.connect((target,port))
		return True

	except:
		return False


for x in range(2000):
	print("Scanning Port: ", x)
	if pscan(x):
		print("Port", x," is open!")
