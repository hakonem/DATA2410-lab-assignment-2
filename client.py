#Client side connects to the server and sends a message to everyone

import socket
import select
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#write server ip and port, and connect
###write your code here###
serverName = socket.gethostbyname(socket.gethostname()) #identify the IP address of the server
serverPort = 17979                                      #determines which server port the client can connect to
client_socket.connect((serverName, serverPort))         #establish connection to server
###your code ends here###

while True:
    inputs = [sys.stdin, client_socket]
    read_sockets, write_socket, error_socket = select.select(inputs,[],[])
    #we check if the message is either coming from your terminal or from the server
    for socks in read_sockets:
        if socks == client_socket:
            #receive message from client and display it on the server side
            #also handle exceptions here if there is no message from the client,
            #you should exit
            ###write your code here###
            data = client_socket.recv(1024)             #message received from client stored in variable
            if not data:                                #exit if-statement if no message received from client
                break
            else:
                print(str(data, 'UTF-8'))           #converts message to string and prints to screen
            ###your code ends here###
        else:
            ###write your code here###
            message = sys.stdin.readline()              #take input from the user
            client_socket.send(message.encode())        #send a message to the server
            ###your code ends here###

client_socket.close()
