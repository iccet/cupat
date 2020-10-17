""" CCC - Global coefficient for adequate scaling speed px,
    else we have abs(vector) >= 1000, what cant be controlable,
    changing this parameter has unobvious consequences, careful.
"""
CONST_CONVERT_COEFFICIENT = CCC = 1 / 100


class BaseObject:
    """ Basic game objects """
    logger = None

    count = 0
    objects = set()

    def __init__(self, name: str = None):
        self.name = name
        self.objects.add(self)
        self.logger.info('Create object: %s', self)

    def __del__(self):
        self.objects.remove(self)
        self.count -= 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if name is None or name in (o.name for o in self.objects):
            self.__name = self._name_gen(self.__class__.__name__)
        else:
            self.count += 1
            self.__name = name

    @classmethod
    def _name_gen(cls, pattern="GameObject"):
        cls.count += 1
        return pattern + "_" + str(cls.count)
