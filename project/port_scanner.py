import socket
from threading import Thread
from queue import Queue

target = #add your ip address
ports = range(1, 1025)
q = Queue()
for port in ports:
    q.put(port)


def scan():
    while not q.empty():
        port = q.get()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"{port} is open")


threads = []
for _ in range(100):
    t = Thread(target=scan)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
print(f"Scan is done!")
