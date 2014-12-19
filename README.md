###一个用redis实现的分布式锁，含有retry和timetout的功能。

* 用with做锁的逻辑语句
* timeout避免了避免了任务出现异常，没有做delete操作
* 对于长时间的业务，增加retry重试锁的次数

```
#coding:utf-8
#my blog: http://xiaorui.cc
from __future__ import with_statement
import redis
import time
from redis_netlock import dist_lock

client = redis.Redis(connection_pool=redis.BlockingConnectionPool(max_connections=15, host='localhost', port=6379))
with dist_lock('test', client):
    time.sleep(10)
    print 'welcome to my blog, http://xiaorui.cc'

```
