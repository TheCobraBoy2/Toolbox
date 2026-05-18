from abc import ABC, abstractmethod

# ha funny video
#https://www.youtube.com/watch?v=mEM0CPeRvbk

class MyType(ABC):
    display_name = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        # Always-required fields
        always_required = ['display_name']
        for attr in always_required:
            if getattr(cls, attr, None) in (None, ''):
                raise TypeError(f"Subclasses of [MyType] must define '{attr}'")

    def __init__(self):
        pass

    @abstractmethod
    def execute(self):
        pass