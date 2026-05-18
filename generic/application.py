from typing import Any
from abc import ABC, abstractmethod

class Application(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def launch(self, args: Any | None = None):
        pass