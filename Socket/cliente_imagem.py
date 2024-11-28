from socket import * 
import os

cliente = socket(AF_INET, SOCK_STREAM)
cliente.connect(( '10.15.135.16' , 4444 ))

file_info = cliente.recv(1024).decode().rstrip()
info = eval(file_info)

with open(info['name']+"_nova_"+".jpg", "wb") as file:
    buffer = cliente.recv(info['size'])
    file.write(buffer)

cliente.close()