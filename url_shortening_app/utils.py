import redis

##############################################################
# Abasract caching logic
###############################################################


def redis_instance():
    # create a redis instance
    return redis.Redis()


class CacheObject(object):
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
