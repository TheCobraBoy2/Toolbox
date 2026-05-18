from abc import abstractmethod, ABCMeta


class Patcher(metaclass=ABCMeta):
    display_name = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        # Always-required fields
        always_required = ['display_name']
        for attr in always_required:
            if getattr(cls, attr, None) in (None, ''):
                raise TypeError(f"Subclasses of [Patcher] must define '{attr}'")

    def __init__(self):
        pass

    @abstractmethod
    def patch(self, args):
        pass