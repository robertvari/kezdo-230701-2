import time, random, threading

def worker1():
    print("Worker 1 started...")
    time.sleep(random.randint(1, 10))
    print("Worker 1 finished.")

def worker2():
    print("Worker 2 started...")
    time.sleep(random.randint(1, 10))
    print("Worker 2 finished.")

def worker3():
    print("Worker 3 started...")
    time.sleep(random.randint(1, 10))
    print("Worker 3 finished.")


thread_1 = threading.Thread(target=worker1)
thread_2 = threading.Thread(target=worker2)
thread_3 = threading.Thread(target=worker3)

thread_1.start()
thread_2.start()
thread_3.start()