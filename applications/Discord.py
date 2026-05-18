from typing import Any

import generic
import util

class Discord(generic.Application):
    display_name = "Discord"

    def launch(self, args: Any | None = None):
        util.launch_or_focus(
            app_name="Discord",
            title_contains="Discord",
        )