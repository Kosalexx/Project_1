""" Decorator, that caches functions. """

storage = {}


def cache_deco(func):
    global storage

    def inner(*args):
        if storage.get(str(args)) is None:
            result = func(*args)
            storage[str(args)] = result
            return result
        else:
            return storage[str(args)]

    return inner
