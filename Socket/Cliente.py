import socket
import os
def cliente():
    for i in range(1):
        msg = input("> ")
        bytesToSend         = ('C:\\Users\\IFPB\\Desktop\testeClienteServidor\\gato.jpg')
        # bytesToSend         = str.encode('C:\\Users\\IFPB\\Desktop\testeClienteServidor\\gato.jpg')
        serverAddressPort   = ("10.15.135.16", 20001)
        bufferSize          = 1024
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)

def server():
    for i in range(1):
        localIP     = "10.15.135.16"
        localPort   = 20010
        bufferSize  = 1024
        msgFromServer       = "Hello UDP Client"
        bytesToSend         = str.encode(msgFromServer)
        UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        UDPServerSocket.bind((localIP, localPort))
        os.system('cls')
        print(" SERVER IMAGEM ONLINE !")
        print()
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        Player = f"Menssagem | {message}"
        print(Player)
        UDPServerSocket.sendto(bytesToSend, address)

while True:
    cliente()
    server()