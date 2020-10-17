from abc import ABC
from base import BaseObject


class AttachableObject(BaseObject, ABC):
    root: BaseObject = None

    def __init__(self, root=None, *args, **kwargs):
        self.root = root
        BaseObject.__init__(self, *args, **kwargs)

    def update(self):
        self.position = self.root.position
