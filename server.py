"""
Server side: it simultaneously handles multiple clients 
and broadcasts when a new client joins or a client 
sends a message.
"""

import socket
import _thread as thread
import time
import sys

#this is to keep all the newly joined connections!
all_client_connections = []

def now():
    return time.ctime(time.time())      #returns the time of day

def handleClient(connection, addr):     #a client handler function
    #this is where we broadcast everyone that a new client has joined
    ###write your code here###
    #append this to the list for broadcast
    #create a message to inform all other clients that a new client has just jo
    all_client_connections.append(connection)
    print(*all_client_connections, sep="\n")
    join_msg = "New user " + str(addr) + " has just joined the server!"
    print(join_msg)
    broadcast2(connection, join_msg)
    ###your code ends here###

    while True:
        message = connection.recv(2048).decode()
        print(now() + " " + str(addr) + "# ",message)
        if ("exit" in message or not message):
            broadcast(connection, f'{addr} left the server')
            connection.close()
            all_client_connections.remove(connection)
            print(*all_client_connections, sep="\n")
            break
        ###write your code here###
        #broadcast this message to the others
        broadcast(connection, message)
        ###your code ends here###

def broadcast(connection, message):
    print("Broadcasting")
    ###write your code here###
    for connection in all_client_connections:
        connection.send(message.encode())
    ###your code ends here###

def broadcast2(connection, message):
    print("Broadcasting")
    ###write your code here###
    for connection in all_client_connections[:-1]:
        connection.send(message.encode())
    ###your code ends here###

def main():
    """
    creates a server socket, listens for new connections,
    and spawns a new thread whenever a new connection joins
    """
    serverName = socket.gethostbyname(socket.gethostname())
    serverPort = 17979
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        #use the bind function wisely!
        ###write your code here###
        serverSocket.bind(('',serverPort))
        #your code ends here
    except:
        print("Bind failed. Error : ")
        sys.exit()
    serverSocket.listen(10)
    print("The server is ready to receive")
    while True:
        ###write your code here###
        (connectionSocket, addr) = serverSocket.accept()
        ###your code ends here###
        print("Server connected by ", addr)
        print("at ", now())
        thread.start_new_thread(handleClient, (connectionSocket, addr))
    serverSocket.close()

if __name__ == "__main__":
    main()
