import time, random

def my_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Process time: {time.time()-start}")
        
        return result
    return wrapper


def check_temperature(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1000:
            print(f"WARNING: TEMPERATURTE IS HIGH {result}")
        
        return result
    return wrapper

@my_timer
def worker():
    print("Worker started...")
    time.sleep(random.randint(1, 10))
    print("Worker finished.")

@my_timer
def worker2():
    print("Worker2 started...")
    time.sleep(random.randint(1, 10))
    print("Worker2 finished.")

@check_temperature
def get_sensor_data1():
    return random.randint(200, 1500)

for i in range(100):
    sensor_result = get_sensor_data1()
    print(sensor_result)