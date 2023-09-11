from time import time
from typing import Callable, TypeVar, ParamSpec


P = ParamSpec('P')
RT = TypeVar('RT')
storage: dict = {}


def cache(cache_time: int = 60) -> Callable[[Callable[P, RT]],
                                            Callable[P, RT]]:
    """ Decorator, that caches functions """
    def inner(func: Callable[P, RT]) -> Callable[P, RT]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> RT:
            global storage
            cache_key = tuple(args)
            if storage.get(cache_key) is None:
                result: RT = func(*args, **kwargs)
                storage[cache_key] = (result, time())
            elif (time() - storage[cache_key][1]) < cache_time:
                storage.pop(cache_key)
                result = func(*args, **kwargs)
            else:
                result = storage[cache_key][0]
            return result
        return wrapper
    return inner
