from socket import *
serverName = '127.0.0.1'
serverPort = 4567
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = "Request a Quote"
clientSocket.sendto(message.encode(), (serverName, serverPort))
response_msg, serverAddress = clientSocket.recvfrom(2048)

print(response_msg.decode())
clientSocket.close()
