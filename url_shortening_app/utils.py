import logging
import redis
import string
import secrets

import requests

##############################################################
# Absracting caching logic
###############################################################


def redis_instance():
    # create a redis instance
    return redis.Redis()


class RedisCache(object):
    def __init__(self):
        self.redis = redis_instance()

    def get(self, key):
        # read cache
        return self.redis.get(str(key))

    def set_(self, key, value):
        # set cache
        self.redis.set(str(key), value)

    def delete(self, key):
        # delete cache
        self.redis.delete(str(key))

    def keys(self):
        # retrieve all keys
        self.redis.keys()


##############################################################
# Absracting random string generation logic
###############################################################


def generate_random_string():
    str = string.ascii_lowercase + string.digits
    random_string = "".join(secrets.choice(str) for i in range(6))
    return random_string


##############################################################
# Absracting url validation logic
###############################################################


def validate_url(passed_url):
    try:
        requests.get(passed_url)
        return True
    except Exception as exc:
        logging.exception(exc)
        return False
