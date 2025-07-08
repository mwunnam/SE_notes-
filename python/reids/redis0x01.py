import redis
import time
import os

r = redis.Redis(host="localhost", port="6379", db=0)

r.setex("auth_token", 10, "Abd332")

while True:
    ttl = r.ttl("auth_token")

    os.system('clear')

    if ttl > 0:
        print(f'Token expires in: {ttl} seconds')
    elif ttl == -1:
        print("Key exits but has no expiry")
        break
    else:
        print("Token expired or does not exit")
        break

    time.sleep(1)
