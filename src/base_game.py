from abc import abstractmethod, ABC
from .core.obj._base import BASIC_SHAPES

from .templates.player import Player
from .templates.wall import Wall
from .templates.random_force import RandomForce
from .core.net.client import Client


class BaseGame(ABC):
    _scene = None
    _player = None
    _gui = None

    def __init__(self, gui):
        self._gui = gui
        # refactor {
        _ppos = self._gui.receive_player_position()
        _psh = self._gui.receive_player_shape()
        _ptc = self._gui.receive_player_track_color()
        _pc = self._gui.receive_player_color()
        _pn = self._gui.receive_player_name()
        # }
        self._player = Player(position=_ppos, shape=BASIC_SHAPES[_psh], color=_pc, track_color=_ptc, name=_pn)
        self._players.append(self._player)

    @abstractmethod
    def scene_init(self): pass

    @abstractmethod
    def random_event(self): pass

    @abstractmethod
    def add_player(self, player): pass

    @abstractmethod
    def update(self): pass

    @abstractmethod
    def render(self, qpainter): pass


class SinglePlayerGame(BaseGame):
    def scene_init(self): pass

    def random_event(self): pass

    def add_player(self, player): pass

    def update(self): pass

    def render(self, qpainter): pass


class MultiPlayerGame(BaseGame):
    _client = None

    def __init__(self, player, gui):
        super().__init__(player, gui)
        self._client = Client(self._player)

    def scene_init(self): pass

    def random_event(self): pass

    def add_player(self, player): pass

    def render(self, qpainter): pass

    def update(self):
        self.client.send()
