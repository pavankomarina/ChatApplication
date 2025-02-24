import errno
import select
import socket
import sys
import threading


HEADER_LENGTH = 20

IP = "127.0.0.1"
PORT = 1234
my_username = input("Username: ")

# Create a socket
# socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
# socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, 
# socket.SOCK_RAW - raw IP packets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a given ip and port
client_socket.connect((IP, PORT))

# Set connection to non-blocking state, so .recv() call won;t block, just return some exception 
# we'll handle
# client_socket.setblocking(False)

# Prepare username and header and send them
# We need to encode username to bytes, then count number of bytes and prepare header of fixed size,
# that we encode to bytes as well
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)


def get_message():
    try:
        # Now we want to loop over received messages (there might be more than one) and print them
        while True:
            # Receive our "header" containing username length, it's size is defined and constant
            username_header = client_socket.recv(HEADER_LENGTH)

            # If we received no data, server gracefully closed a connection, for example using
            # socket.close() or socket.shutdown(socket.SHUT_RDWR)
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()

            # Convert header to int value
            username_length = int(username_header.decode('utf-8').strip())

            # Receive and decode username
            username = client_socket.recv(username_length).decode('utf-8')
            # split here again to get the from_user and message
            data = username.split('*|*')
            if len(data) > 1:
                username = data[0]
                message = data[1]
                print(f'{username} > {message}\n')

    except IOError as e:
        # This is normal on non blocking connections - when there are no incoming data error is 
        # going to be raised. Some operating systems will indicate that using AGAIN, and some
        # using WOULDBLOCK error code. We are going to check for both - if one of them - that's
        # expected, means no incoming data, continue as normal. If we got different error code, 
        # then something happened
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

    except Exception as e:
        # Any other exception - something happened, exit
        print('Reading error: '.format(str(e)))
        sys.exit()

# running seoarate thread to show messages sent by other users
t1 = threading.Thread(target=get_message)
t1.start()
# get_message()

while True:

    to_user = input('Enter username to send message or type "all" to send to all :')
    message = input(f'{my_username} > ')

    # If message is not empty - send it
    if message and to_user:
        # add both to_user and message and send it to user
        message = message + '*|*' + to_user
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)
