from root import RootObject
from interfaces.idynamic import IDynamic


class AttachableObject(RootObject, IDynamic):
    root: RootObject = None

    def __init__(self, root=None, *args, **kwargs):
        self.root = root
        RootObject.__init__(self, root.position)

    def update(self):
        self.position = self.root.position
