import redis 
from time import sleep

r0 = redis.Redis(host='localhost', port=6379, db=0)

r0.set('name', 'Michael')
r0.incr("login_count")
value = r0.get('name')
login_count = r0.get("login_count")

auth_token = r0.get('auth_token')

if value:
    print(value.decode())
    print(login_count.decode())
else:
    print("key 'name' not found in db 0")
