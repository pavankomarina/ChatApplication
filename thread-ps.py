import threading
from queue import Queue
import socket
import time

print_lock = threading.Lock()
target = input("What IP Address to scan:")

def portscan(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		connect = s.connect((target,port))
		with print_lock:
			print("Port: ", port)

		connect.close()

	except:
		pass

def threader():
	while True:
		worker = q.get()
		portscan(worker)
		q.task_done()

q = Queue()

for x in range (10000):
	t = threading.Thread(target=threader)
	t.daemon = True
	t.start()
	#print("x = ", x)

for worker in range(1,65000):
	q.put(worker)
	#print("worker = ", worker)

#print("Port = ", port)
q.join()


