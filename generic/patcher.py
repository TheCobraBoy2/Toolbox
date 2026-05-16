class Patcher:
    display_name = "Generic Patcher"
    def __init__(self):
        pass

    def patch(self, args):
        print("Generic Patch Message", args)

if __name__ == "__main__":
    p = Patcher()
    p.patch()