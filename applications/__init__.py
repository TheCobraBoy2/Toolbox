import pkgutil
import importlib
import inspect

from generic import Application as CompType

def get_all_apps():
    patchers_list = []

    for _, module_name, _ in pkgutil.iter_modules(__path__):
        module = importlib.import_module(f"{__name__}.{module_name}")
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, CompType) and obj is not CompType:
                patchers_list.append(obj())

    return patchers_list