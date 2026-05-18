from typing import Any

import generic
import util

class Everything(generic.Application):
    display_name = "Everything"

    def launch(self, args: Any | None = None):
        util.launch_or_focus(
            app_name="Everything",
            title_contains="Everything",
            maximize=False
        )