# import socket module
from socket import *
import sys  # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM) #the server socket is created
#Prepare a server socket
# Fill in start
serverPort = 1000
serverSocket.bind(('', serverPort)) # assigns the port number to the socket.
serverSocket.listen(1) #Lets the server listen for TCP connection requests from the client.
# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    # Accept method invoked creating new socket in the server unique to the clients address.
    connectionSocket, addr =  serverSocket.accept()
    try:
        message =  connectionSocket.recv(1024).decode() #blocking call limits socket to read 1024 bytes.
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata =  f.read()
        # Send one HTTP header line into socket
        # Fill in start
        # Indicates server is using HTTP/1.1 Request succeeded and the information is returned in the response.
        statusLine = "HTTP/1.1 200 OK\r\n"
        #Tells the client it will close the TCP connection after sending the message.
        headerLine = "Connection: close\r\n"
        connectionSocket.send(statusLine.encode()) #encodes the string faster
        connectionSocket.send(headerLine.encode())
        connectionSocket.send("\r\n".encode())
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
# Send response message for file not found
# Fill in start
        errorMsg = "HTTP/1.1 404 Not Found\r\n"
        connectionSocket.send(errorMsg.encode())
        connectionSocket.send("\r\n".encode())
# Fill in end
# Close client socket
# Fill in start
        connectionSocket.close()
# Fill in end
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
