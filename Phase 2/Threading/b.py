import threading
import queue
import time

task_queue = queue.Queue()

def producer():
    for i in range(10):
        task_queue.put(f"task-{i}")
        print(f"[producer] queued task-{i}")
    task_queue.put(None)  # sentinel: signals "no more work"

def consumer(name):
    while True:
        task = task_queue.get()
        if task is None:
            task_queue.put(None)  # re-signal for other consumers
            break
        print(f"[{name}] processing {task}")
        time.sleep(0.3)
        task_queue.task_done()

producer_thread = threading.Thread(target=producer)
consumer_threads = [threading.Thread(target=consumer, args=(f"Consumer-{i}",)) for i in range(3)]

producer_thread.start()
for c in consumer_threads:
    c.start()

producer_thread.join()
for c in consumer_threads:
    c.join()