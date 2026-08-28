import socket
import threading
import queue

target = "scanme.nmap.org"
start_port = 20
end_port = 100
num_threads = 20
timeout = 1.0
port_queue = queue.Queue()
for port in range(start_port, end_port + 1):
    port_queue.put(port)

print_lock = threading.Lock()


def scan_worker():
    while True:
        try:
            port = port_queue.get_nowait()
        except queue.Empty:
            return

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            sock.connect((target, port))
            banner = None
            try:
                sock.settimeout(timeout)
                data = sock.recv(1024)
                if data:
                    banner = data.decode().strip()
            except socket.timeout:
                pass
            with print_lock:
                print(f"[Open ] port {port} banner {banner}")
        except ConnectionRefusedError:
            pass
        except socket.timeout:
            pass
        except OSError:
            pass
        finally:
            sock.close()
            port_queue.task_done()


threads = []
for _ in range(num_threads):
    t = threading.Thread(target=scan_worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Task is done")
