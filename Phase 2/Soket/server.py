import socket

host = '0.0.0.0' 
port = 2223
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
print(f"Server is running at: {host}\n")
while True:
    conn,addr=server.accept()
    print(f"Hello from server address:{addr}")
    messege=conn.recv(1024).decode('utf-8')
    print(f"Server is responding to {messege}")
    conn.send(f"This is from server baby".encode('utf-8'))
    conn.close()