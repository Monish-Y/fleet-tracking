import time
import random
from http.client import responses

import requests

Base_URL = "http://127.0.0.1:8000"

vehicles = {
    1:{"lat":10.251, "lon":55.789},
    2:{"lat":15.174, "lon":74.123},
    3:{"lat":12.159, "lon":80.159},
}

def update_vehicle(vehicle_id, latitude, longitude):
    try:
        response = requests.post(f"{Base_URL}/vehicle/update",
                                 params={
                                     "id":vehicle_id,
                                     "latitude":latitude,
                                     "longitude":longitude
                                 })
        print(f"Vehicle {vehicle_id} updated:", response.status_code)
    except Exception as e:
        print("Error:",e)

while True:
    for vid, coords in vehicles.items():
        # Slight movement simulation
        coords["lat"] += random.uniform(-0.001, 0.001)
        coords["lon"] += random.uniform(-0.001, 0.001)

        update_vehicle(vid, coords["lat"], coords["lon"])

    time.sleep(2)