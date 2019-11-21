from socket import *
import sys

# Get address and port from parameters
try:
    serverAddress = str(sys.argv[1])
    serverPort = int(sys.argv[2])
    fileName = ''
    keepConnectionAlive = False
    if len(sys.argv) >= 4:
        fileName = str(sys.argv[3])
    if len(sys.argv) >= 5:
        if str(sys.argv[4]).lower() in ["true", "keepalive"]:
            keepConnectionAlive = True

except IndexError:
    print("You need to specify an address and port.")
    print("Usage: client.py <server_host> <server_port> <filename (optional)> <keep_connection_alive (optional)>")
    sys.exit()

print("Retrieving {} from {}:{}\n".format(fileName, serverAddress, serverPort))

# Create socket
socket = socket(AF_INET, SOCK_STREAM)
# Connect socket to specified address and port
socket.connect((serverAddress, serverPort))

# Send HTTP GET request to server for specified file
request = 'GET /{} HTTP/1.1\r\nHost: {}:{}\r\n\r\n'.format(fileName, serverAddress, serverPort)
request = request.encode()
socket.send(request)

# Obtain response from server and print it out as it comes
while True:
    data = socket.recv(1024).decode()
    print(data, end='')
    # Exit loop when server is not providing any more data
    if not keepConnectionAlive and not data:
        break

# Close the socket, print the response, and exit
socket.close()
sys.exit()


