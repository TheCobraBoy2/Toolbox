import pkgutil
import importlib
import inspect
import os

from generic import MyType as CompType

from .subnet_calculator import SubnetCalculator

PLUGIN_DIR = os.path.join(os.path.expanduser("~"), ".toolbox", "mod", "custom")

class PluginAPI:
    def __init__(self):
        import generic
        import util

        self.generic = generic
        self.util = util

api = PluginAPI()
def load_external_things():
    patchers = []

    os.makedirs(PLUGIN_DIR, exist_ok=True)

    for file in os.listdir(PLUGIN_DIR):
        if not file.endswith(".py"):
            continue

        file_path = os.path.join(PLUGIN_DIR, file)
        module_name = f"external_{file[:-3]}"

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec is None or spec.loader is None:
            continue

        module = importlib.util.module_from_spec(spec)
        module.api = api
        spec.loader.exec_module(module)

        # find patcher classes
        for _, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, CompType) and obj is not CompType:
                patchers.append(obj())

    return patchers

def get_all_things():
    patchers = []

    import inspect
    import sys

    for mod in sys.modules.values():
        if not hasattr(mod, "__name__"):
            continue

        if not mod.__name__.startswith(__name__ + "."):
            continue

        for _, obj in inspect.getmembers(mod, inspect.isclass):
            if issubclass(obj, CompType) and obj is not CompType:
                patchers.append(obj())
    patchers.extend(load_external_things())
    return patchers