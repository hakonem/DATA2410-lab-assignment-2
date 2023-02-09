from socket import *
import sys

serverName = gethostbyname(gethostname())
serverPort = 17979
clientSocket = socket(AF_INET, SOCK_STREAM)
try:
    clientSocket.connect((serverName,serverPort))
except:
    print("ConnectionError")
    sys.exit()
while True:
    instr = input('Input instruction: ')
    clientSocket.send(instr.encode())
    #modifiedSentence = clientSocket.recv(1024)
    #print ('From Server:', modifiedSentence.decode())
    if (instr == "broadcast"):
        msg = input('Input message for broadcast: ')
        clientSocket.send(msg.encode())
        msg_recv = clientSocket.recv(1024)
        print('From Server:', msg_recv.decode())
    if (instr == "exit"):
        break


clientSocket.close()