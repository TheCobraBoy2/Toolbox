import generic

class patch(generic.Patcher):
    def patch(self, args):
        print("patch called" + args.get("name"))