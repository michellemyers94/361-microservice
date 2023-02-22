from socket import *


serverPort = 4567
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    # response_msg = f"\n\n\n\nResponse Message: \n {modifiedMessage}"
    response_msg = "Genius is one percent inspiration and ninety-nine percent perspiration - Thomas Edison"
    serverSocket.sendto(response_msg.encode(), clientAddress)


