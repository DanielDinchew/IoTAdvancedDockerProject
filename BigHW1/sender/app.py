import threading
import time
import random
import requests

num_sensors = 3

def simulate_sensor_data(sensor_id):
    while True:
        timestamp = time.time()
        device_id = f"{sensor_id}"
        data = {
            "timestamp": timestamp,
            "device_id": device_id
        }
        requests.post('http://server:6000/data', json=data)
        time.sleep(random.uniform(1, 5))
threads = []
for sensor_id in range(1, num_sensors + 1):
    thread = threading.Thread(target=simulate_sensor_data, args=(sensor_id,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()