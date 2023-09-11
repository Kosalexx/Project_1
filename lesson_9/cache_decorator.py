from typing import Callable, TypeVar, ParamSpec


P = ParamSpec('P')
RT = TypeVar('RT')
storage: dict = {}


def cache_deco(func: Callable[P, RT]) -> Callable[P, RT]:
    """ Decorator, that caches functions. """
    global storage

    def inner(*args: P.args, **kwargs: P.kwargs) -> RT:
        if storage.get(tuple(args)) is None:
            result: RT = func(*args, **kwargs)
            storage[tuple(args)] = result
            return result
        else:
            result = storage[tuple(args)]
            return result
    return inner
