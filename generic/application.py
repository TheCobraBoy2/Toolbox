from typing import Any
from abc import ABCMeta, abstractmethod

class Application(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def launch(self, args: Any | None = None):
        pass