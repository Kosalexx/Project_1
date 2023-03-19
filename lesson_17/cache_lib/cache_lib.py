from time import time
from typing import Type, TypeVar, Any, Callable


simple_storage: dict[tuple,] = {}
lru_storage: dict[tuple,] = {}
fifo_storage: dict[tuple,] = {}
ttl_storage: dict[tuple,] = {}


class SimpleCache:
    """Stores already computed keys and returns the cached result.

    It has no limitations on the size and time of the information storage.
    """
    def __call__(self, func: Callable[[Any], Any]) -> Any:
        def wrapper(*args: Any):
            cache_key: tuple = tuple(args)
            if simple_storage.get(cache_key) is None:
                result: Any = func(*args)
                simple_storage[cache_key] = result
            else:
                result: Any = simple_storage[cache_key][0]
            return result
        return wrapper


class FIFOCache:
    """First int first out cache.

    When creating this cache, the maximum possible cache size is set.
    If you need to add a new item when the limit is reached, the oldest
    item (by date of adding to the cache) is removed first,
    and then a new one is added.

    :param max_size: maximum possible size of elements in cache.
                     Default = 10.
    :type max_size: int

    :raises ValueError: if 'max_size' of storage not integer.
    """
    def __init__(self, max_size: int = 10) -> None:
        self.max_size = max_size

    @property
    def max_size(self):
        return self._max_size

    @max_size.setter
    def max_size(self, value):
        if not isinstance(value, int):
            raise ValueError("Max size of the storage must be integer.")
        self._max_size = value

    def __call__(self, func: Callable[[Any], Any]) -> Any:
        def wrapper(*args: Any):
            cache_key: tuple = tuple(args)
            current_length: int = len(fifo_storage)
            if fifo_storage.get(cache_key) is not None:
                result: Any = fifo_storage.get(cache_key)[0]
            else:
                if current_length < self.max_size:
                    result: Any = func(*args)
                    fifo_storage[cache_key] = (result, time())
                else:
                    max_value: float = time()
                    for keys, values in fifo_storage.items():
                        if values[1] < max_value:
                            key = keys
                            max_value = values[1]
                    fifo_storage.pop(key)
                    result: Any = func(*args)
                    fifo_storage[cache_key] = (result, time())
            return result
        return wrapper


class LRUCache:
    """Least recently used cache.

    When creating this cache, the maximum possible cache size is set.
    If you need to add a new item when the limit is reached, the oldest
    item (by the time of access to the element) is removed first,
    and then a new one is added.

    Like FIFOCache has a maximum size, but unlike FIFOCache, when you
    reach the limit is removed the oldest element NOT by time
    of addition, but by the time of access to the element.

    :param max_size: maximum possible size of elements in cache.
                     Default = 10.
    :type max_size: int

    :raises ValueError: if 'max_size' of storage not integer.
    """
    def __init__(self, max_size: int = 10) -> None:
        self.max_size = max_size

    @property
    def max_size(self):
        return self._max_size

    @max_size.setter
    def max_size(self, value):
        if not isinstance(value, int):
            raise ValueError("Max size of the storage must be integer.")
        self._max_size = value

    def __call__(self, func: Callable[[Any], Any]) -> Any:
        def wrapper(*args: Any):
            cache_key: tuple = tuple(args)
            current_length: int = len(lru_storage)
            if lru_storage.get(cache_key) is not None:
                result: Any = lru_storage.get(cache_key)[0]
                lru_storage.pop(cache_key)
                new_val = (result, time())
                lru_storage[cache_key] = new_val
            else:
                if current_length < self.max_size:
                    result: Any = func(*args)
                    lru_storage[cache_key] = (result, time())
                else:
                    max_value = time()
                    for keys, values in lru_storage.items():
                        if values[1] < max_value:
                            key = keys
                            max_value = values[1]
                    lru_storage.pop(key)
                    result = func(*args)
                    lru_storage[cache_key] = (result, time())
            return result
        return wrapper


class TTLCache:
    """Time to live cache.

    A variant of 'LRUCache', but the lifetime of the cache entry is added
    (specified in seconds) and correspondingly besides the time of last
    access to the element the lifetime is also analyzed.

    :param max_size: maximum possible size of elements in cache.
                     Default = 10.
    :type max_size: int
    :param ttl: lifetime of the record in cache. Default = 600
    :type ttl: int

    :raises ValueError: if 'max_size' of storage and 'ttl' are not integer.
    """
    def __init__(
            self,
            max_size: int = 10,
            ttl: int = 600
            ) -> None:
        self.max_size = max_size
        self.ttl = ttl

    @property
    def max_size(self):
        return self._max_size

    @max_size.setter
    def max_size(self, value):
        if not isinstance(value, int):
            raise ValueError("Max size of the storage must be integer.")
        self._max_size = value

    @property
    def ttl(self):
        return self._ttl

    @ttl.setter
    def ttl(self, value):
        if not isinstance(value, int):
            raise ValueError("'Time to live' value must be integer.")
        self._ttl = value

    def __call__(self, func: Callable[[Any], Any]) -> Any:
        def wrapper(*args: Any):
            cache_key: tuple = tuple(args)
            current_length: int = len(ttl_storage)
            if ttl_storage.get(cache_key) is not None:
                time_of_insert: float = ttl_storage.get(cache_key)[1]
                if (time() - time_of_insert) > self.ttl:
                    result: Any = func(*args)
                else:
                    result: Any = ttl_storage.get(cache_key)[0]
                ttl_storage.pop(cache_key)
                new_val = (result, time())
                ttl_storage[cache_key] = new_val
            else:
                if current_length < self.max_size:
                    result: Any = func(*args)
                    ttl_storage[cache_key] = (result, time())
                else:
                    max_value = time()
                    for keys, values in ttl_storage.items():
                        if values[1] < max_value:
                            key = keys
                            max_value = values[1]
                    ttl_storage.pop(key)
                    result = func(*args)
                    ttl_storage[cache_key] = (result, time())
            return result
        return wrapper


existing_cache = (SimpleCache, FIFOCache, LRUCache, TTLCache)
Cache_types = TypeVar("Cache_types", *existing_cache)


class Cached:
    """Basic Decorator Class. It is used to cache wrappable functions.

    Takes as its argument an object of one of the available decorator classes.
    Available decorators: SimpleCache, FIFOCache, LRUCache, TTLCache.

    :param cache: object of one of available decorator classes
    :type cache: Callable[[Type[Cache_types]], Any]

    :raises ValueError: if object of an unsupported decorator class is passed.
    """
    def __init__(self, cache: Callable[[Type[Cache_types]], Any]) -> None:
        self.cache = cache

    def _validate_cache(self, value):
        if not isinstance(value, existing_cache):
            raise ValueError("Non-existent caching provider. Possible "
                             "options: SimpleCache, LRUCache, FIFOCache, "
                             "TTLCache.")

    @property
    def cache(self):
        return self._cache

    @cache.setter
    def cache(
            self,
            value: Callable[[Type[Cache_types]], Any]
            ) -> Callable[[Type[Cache_types]], Any]:
        self._validate_cache(value)
        self._cache = value

    def __call__(self, func: Callable[[Any], Any]) -> Any:
        result = self.cache(func)
        return result
