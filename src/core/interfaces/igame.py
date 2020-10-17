from abc import abstractmethod, ABC
from idynamic import IDynamic
from irender import IRender


class IGame(IDynamic, IRender, ABC):

    @abstractmethod
    def scene_init(self): pass

    @abstractmethod
    def random_event(self): pass

    @abstractmethod
    def add_player(self, player): pass

