from socket import * # Imports socket library

server_sd = socket(AF_INET, SOCK_STREAM) #Creates socket, AF_INET -> Address family (IPV4) - SOCK_STREAM -> TCP Socket
server_ip = gethostbyname(gethostname())   #Gets IP of your computer
print(server_ip)
port = 17979    #Port can be whatever you want, find one that is not used by other services

server_sd.bind((server_ip,port))     #Assigns IP and port to the created socket
server_sd.listen()     #Starts listening for connections
conn_sd, addr = server_sd.accept() #Server waits for connections, accepts any incoming
received_line = conn_sd.recv(1024).decode() #Receives and decodes message
print(received_line)  #Prints received message
conn_sd.send(received_line.encode())    #Send message back to client
#Close sockets server side
conn_sd.close()
server_sd.close()