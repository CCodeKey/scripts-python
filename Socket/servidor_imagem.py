from socket import * 
import os

server = socket(AF_INET, SOCK_STREAM)
server.bind(( '10.15.135.16' , 4444 ))
server.listen(5)

while True:
    os.system('cls')
    print(" SERVER IMAGEM ONLINE !")
    print()
    obj, add = server.accept()

    try:
        file_path = os.path.join('gato.jpg')
        file_size = os.path.getsize(file_path)
        file_name = file_path.split(".")[0]
        file_extension = file_path.split(".")[1]

        file_info = str({
            "path": file_path,
            "size": file_size,
            "name": file_name,
            "extension" : file_name
        }).encode()

        obj.send(file_info)

        with open(file_path, "rb") as file:
            obj.send(file.read(file_size))
        obj.close() 

    except Exception as ex:
        print(ex)