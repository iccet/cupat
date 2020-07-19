from abc import abstractmethod, ABC

from .core.net.client import Client


class BaseGame(ABC):
    scene = None
    player = None

    def __init__(self):
        self._players.append(self.player)

    @abstractmethod
    def scene_init(self): pass

    @abstractmethod
    def random_event(self): pass

    @abstractmethod
    def add_player(self, player): pass

    @abstractmethod
    def update(self): pass

    @abstractmethod
    def render(self): pass


class SinglePlayerGame(BaseGame):
    def scene_init(self): pass

    def random_event(self): pass

    def add_player(self, player): pass

    def update(self): pass

    def render(self): pass


class MultiPlayerGame(BaseGame):
    client = None

    def __init__(self):
        super().__init__()
        self.client = Client(self.player)

    def scene_init(self): pass

    def random_event(self): pass

    def add_player(self, player): pass

    def render(self): pass

    def update(self):
        self.client.send()
