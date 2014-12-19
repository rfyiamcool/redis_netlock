from __future__ import with_statement
import redis
import time
from redis_lock import dist_lock

client = redis.Redis(connection_pool=redis.BlockingConnectionPool(max_connections=15, host='localhost', port=6379))
with dist_lock('test', client):
    print 'Is there anybody out there!?'

