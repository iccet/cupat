from src.base_game import *
from src.templates.random_force import RandomForce
from src.core.obj.force import ParasiteForceRender
from src.templates.wall import Wall


class Tron(SinglePlayerGame):
    _players = []
    __scene_objects = []
    _random_force = None

    def __init__(self):
        super().__init__()
        self.scene_init()
        self._random_force_render = ParasiteForceRender(self._random_force)

    def scene_init(self):
        self._random_force = RandomForce(self.player)
        self._random_force.random()

        wall = Wall(name="Wall", position=[100, 100], scaling=(50, 500))
        self.__scene_objects.append(wall)
        wall = Wall(name="Wall", position=[900, 200], scaling=(100, 100))
        self.__scene_objects.append(wall)
        wall = Wall(name="Wall", position=[1600, 200], scaling=(10, 500))
        self.__scene_objects.append(wall)

        wall = Wall(name="Wall", position=[500, 500], scaling=(100, 100))
        self.__scene_objects.append(wall)
        wall = Wall(name="Wall", position=[500, 900], scaling=(500, 100))
        self.__scene_objects.append(wall)

    def random_event(self):
        self._random_force.random()

    def add_player(self, player):
        self._players.append(player)

    def update(self):
        if self.player.ready:

            self._random_force.update()

            # for obj in self.__scene_objects:
            #     self._random_force.in_collision(obj)
            #     obj.in_collision(obj, *self.__scene_objects, *self._players)
            #     obj.update()

            for player in self._players:
                # self._random_force.in_collision(player)
                player.in_collision(player, *self._players, *self.__scene_objects)
                player.update()

    def render(self):
        if self.player.ready:

            for player in self._players:
                player.render()

            for obj in self.__scene_objects:
                obj.render()

            self._random_force_render.render()
