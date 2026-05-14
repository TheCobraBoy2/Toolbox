from typing import Any

import generic
from AppOpener import open

class TestApp(generic.Application):
    def launch(self, args: Any | None = None):
        open("Everything")