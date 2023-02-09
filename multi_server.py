"""
Server side: open a socket on a port, listen for a message
from a client, and send an echo reply;
echoes lines until eof when client closes socket; spawns a
thread to handle each client connection; threads share global
memory space with main thread.
"""
import threading
from socket import *
import _thread as thread
import time

"""
def now():

    return time.ctime(time.time())    #returns the time of day
"""

def handleClient(connection):      #a client handler function

    while True:
        data = connection.recv(1024).decode()
        print ("received instruction = ", data)
        #modified_message = data.upper()
        #connection.send(modified_message.encode())
        if (data == "broadcast"):
            broadcast(connection, list)
        if (data == "exit"):
            break
    connection.close()

def broadcast(connection, clients):
    message = connection.recv(1024).decode()
    print("received broadcast message = ", message)
    #print(*clients, sep = "\n")
    #connection.send(message.encode())
    for client in [clients]:
        connection.send(message.encode())



def main():
    """
    creates a server socket, listens for new connections,
    and spawns a new thread whenever a new connection join
    """
    serverPort = 17979
    serverSocket = socket(AF_INET,SOCK_STREAM)
    clients = []
    try:
        serverSocket.bind(('',serverPort))
    except:
        print("Bind failed. Error : ")
    serverSocket.listen(1)
    print('The server is ready to receive')
    while True:
        connectionSocket, addr = serverSocket.accept()
        clients.append(addr)
        print(*clients, sep = "\n")
        #print('Server connected by ', addr)
        #print('at ', now())
        thread.start_new_thread(handleClient, (connectionSocket,))
    serverSocket.close()

if __name__ == '__main__':
    main()