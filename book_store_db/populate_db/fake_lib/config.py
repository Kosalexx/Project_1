import inspect
from . import providers

PROVIDERS = [names for names, obj in inspect.getmembers(providers)
             if inspect.isclass(obj)]

SUPPORTED_DB = ['first_names.txt', 'last_names.txt']
