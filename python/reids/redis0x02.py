import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.rpush("today_task", "read books", "go to work", "sleep")

today_task = r.get('today_task')

for task in today_task.decode():
    print(task)
