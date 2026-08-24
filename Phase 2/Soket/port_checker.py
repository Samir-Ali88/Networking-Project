import socket
host = '127.0.0.1' 
port = 8000
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.settimeout(1)
result=client.connect_ex((host,port))
if result==0:
    print(f" {port} is open")

else:
     print(f"{port} is closed!!!!")

client.close()