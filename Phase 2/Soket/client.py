import socket

host = '0.0.0.0' 
port = 2223
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
client.send("Hello Server!".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))
client.close()
