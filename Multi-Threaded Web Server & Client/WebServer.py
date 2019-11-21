# import socket module
from socket import *
import sys  # In order to terminate the program
import threading

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a server socket
# Fill in start
serverPort = 1000
serverSocket.bind(('', serverPort))


class ClientThread(threading.Thread):
    def run(self):
        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            # Send one HTTP header line into socket
            # Fill in start
            statusLine = "HTTP/1.1 200 OK\r\n"
            headerLine = "Connection: close\r\n"
            connectionSocket.send(statusLine.encode())
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
while True:
    serverSocket.listen(1)
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    newThread = ClientThread()
    newThread.start()

# Fill in end
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
