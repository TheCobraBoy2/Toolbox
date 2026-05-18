from typing import Any

import generic
import util

class Spotify(generic.Application):
    display_name = "Spotify"

    def launch(self, args: Any | None = None):
        util.launch_or_focus(
            app_name="Spotify",
            title_contains="Spotify",
        )