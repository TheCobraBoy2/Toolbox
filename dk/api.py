from __future__ import annotations

import generic
import util


class PluginAPI:
    def __init__(self) -> None:
        self.generic = generic
        self.util = util