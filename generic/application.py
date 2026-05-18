from typing import Any
from abc import ABCMeta, abstractmethod

class Application(metaclass=ABCMeta):
    display_name = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        # Always-required fields
        always_required = ['display_name']
        for attr in always_required:
            if getattr(cls, attr, None) in (None, ''):
                raise TypeError(f"Subclasses of [Application] must define '{attr}'")

    def __init__(self):
        pass

    @abstractmethod
    def launch(self, args: Any | None = None):
        pass