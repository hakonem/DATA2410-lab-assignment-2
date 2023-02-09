from socket import *        #Imports socket library

msg = "Hello world!"
client_sd = socket(AF_INET, SOCK_STREAM)    #See server.py
server_ip = gethostbyname(gethostname())   #Gets IP of your computer
port = 17979    #Port that is used on server
client_sd.connect((server_ip, port))     #Connects socket to given IP and port
client_sd.send(msg.encode())     #Send encoded message
received_line = client_sd.recv(1024).decode()   #Read data from the socket
print(received_line)    #Print message
client_sd.close()   #Close socket client side

