from redis import Redis
from rq import Queue
from  mail_auto import automatic

q = Queue(connection=Redis())

result = q.enqueue(
             automatic)