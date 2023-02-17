#Client side connects to the server and sends a message to everyone

import socket
import select
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#write server ip and port, and connect
###write your code here###
serverName = socket.gethostbyname(socket.gethostname())
serverPort = 17979
client_socket.connect((serverName, serverPort))
###your code ends here###

while True:
    inputs = [sys.stdin, client_socket]
    read_sockets, write_socket, error_socket = select.select(inputs,[],[])
    #we check if the message is either coming from your terminal or from as server
    for socks in read_sockets:
        if socks == client_socket:
            #receive message from client and display it on the server side
            #also handle exceptions here if there is no message from the client,
            #you should exit
            ###write your code here###
            data = client_socket.recv(1024)
            if not data:
                break
            else:
                print("New message: " + str(data, 'UTF-8'))
            ###your code ends here###
        else:
            #takes input from the user
            message = sys.stdin.readline()
            #send a message to the server
            ###write your code here###
            client_socket.send(message.encode())
            ###your code ends here###

client_socket.close()
