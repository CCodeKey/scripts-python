import socket
import os

def cliente():
    for i in range(1):
        msg = input("> ")
        envio = str.encode(msg)
        serverAddressPort   = ("10.15.135.16", 20010)
        bufferSize          = 1024
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        UDPClientSocket.sendto(envio, serverAddressPort)
        UDPClientSocket.recvfrom(bufferSize)

def server():
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    Player = f"Menssagem | {message}"
    print(Player)
    UDPServerSocket.sendto(bytesToSend, address)

localIP     = "10.15.135.16"
localPort   = 20001
bufferSize  = 1024
msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
os.system('cls')
print(" SERVER IMAGEM ONLINE !")    
print()
while(True):
    server()
    cliente()