import pkgutil
import importlib
import inspect

from generic import Patcher

def get_all_patchers():
    patchers_list = []

    for _, module_name, _ in pkgutil.iter_modules(__path__):
        module = importlib.import_module(f"{__name__}.{module_name}")
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, Patcher) and obj is not Patcher:
                patchers_list.append(obj())

    return patchers_list