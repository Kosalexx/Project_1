""" Decorator, that caches functions. """
from time import time


storage = {}


def cache(cache_time=60):
    def inner(func):
        def wrapper(*args):
            global storage
            cache_key = str(args)

            if storage.get(cache_key) is None:
                result = func(*args)
                storage[cache_key] = (result, time())
            elif (time() - storage[cache_key][1]) < cache_time:
                storage.pop(cache_key)
                result = func(args)
            else:
                result = storage[cache_key][0]

            return result
        return wrapper
    return inner
