import time, random

def my_timer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

def worker():
    print("Worker started...")
    time.sleep(random.randint(1, 10))
    print("Worker finished.")

start = time.time()
worker()
print(f"Process time: {time.time()- start}")