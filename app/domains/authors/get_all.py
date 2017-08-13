class GetAll:
    def __init__(self, root):
        self.root = root
        self.objects = []

    def __call__(self):
        self.objects = list(self.root.authors.values())
        return self.objects
