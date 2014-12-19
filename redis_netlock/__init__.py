"""
    redis_netlock
    ~~~~~~~~~~~~~~

    Implements a distributed transaction using redis or
    a memcached compatible storage.

    Example::

        from __future__ import with_statement
        import redis
        from redis_lock import dist_lock

        client = redis.Redis(connection_pool=redis.BlockingConnectionPool(max_connections=15, host='localhost', port=6379))
        with dist_lock('test', client):
            print 'Is there anybody out there!?'

    :copyright: 2014 by ruifengyun .
    :license: BSD
"""

from __future__ import with_statement

import time

from contextlib import contextmanager
from random import random

DEFAULT_EXPIRES = 15
DEFAULT_RETRIES = 5

@contextmanager
def dist_lock(key, client):
    key = 'lock_%s' % key

    try:
        _acquire_lock(key, client)
        yield
    finally:
        _release_lock(key, client)

def _acquire_lock(key, client):
    for i in xrange(0, DEFAULT_RETRIES):
        get_stored = client.get(key)
        if get_stored:
            sleep_time = (((i+1)*random()) + 2**i) / 2.5
            print 'Sleeipng for %s' % (sleep_time)
            time.sleep(sleep_time)
        else:
            stored = client.set(key, 1)
            client.expire(key,DEFAULT_EXPIRES)
            return
    raise Exception('Could not acquire lock for %s' % key)

def _release_lock(key, client):
    client.delete(key)
