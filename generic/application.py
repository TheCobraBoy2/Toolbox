from typing import Any

class Application:
    def __init__(self):
        pass

    def launch(self, args: Any | None = None):
        print("Generic Application Message", args)

if __name__ == "__main__":
    p = Application()
    p.launch()