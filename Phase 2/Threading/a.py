import threading
import time
def worker(name,delay):
    print(f"Worker [{name}] Starting \n")
    time.sleep(delay)
    print(f"Wrok done by [{name }]\n")

threads=[]
for i in range (5):
    t=threading.Thread(target=worker,args=(f"Worker -{i}",1))
    threads.append(t)
    t.start()

for ti in threads:
    ti.join()