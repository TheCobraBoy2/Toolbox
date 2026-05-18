import time
from functools import wraps

def exectime(name=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{wrapper.__name__} took {end - start:.4f} seconds")
            return result
        # override the function name if provided
        if name:
            wrapper.__name__ = name
        return wrapper
    return decorator