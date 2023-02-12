""" Decorator, that caches functions. """


def cache_deco(func):
    storage = {}

    def inner(*args):
        if storage.get(str(args)) is None:
            result = func(*args)
            storage[str(args)] = result
            return result
        else:
            return storage[str(args)]

    return inner
