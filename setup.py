#coding:utf-8
#!/usr/bin/env python

import os
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup

def list_files(path):
    for fn in os.listdir(path):
        if fn.startswith('.'):
            continue
        fn = os.path.join(path, fn)
        if os.path.isfile(fn):
            yield fn

setup(name='redis_netlock',
      version = '1.1',
      author="ruifengyun",
      author_email="rfyiamcool@163.com",
      url="http://xiaorui.cc/",
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      packages=['redis_netlock'],
      platforms=["Any"],
      license="BSD",
      keywords='redis lock distributed',
      description="一个用redis做的分布式锁，含有超时及重试机制.",
      long_description="""\
redis_netlock
---------------

Implements a distributed transaction using redis or
a redis compatible storage.


Example
-------

Basic example of usage::

from __future__ import with_statement
import redis
import time
from redis_netlock import dist_lock

client = redis.Redis(connection_pool=redis.BlockingConnectionPool(max_connections=15, host='localhost', port=6379))
with dist_lock('test', client):
    time.sleep(10)
    print 'welcome to my blog, http://xiaorui.cc'

""")
