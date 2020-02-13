from src.base_game import *


class Tron(SinglePlayerGame):
    _players = []
    __scene_objects = []
    _random_force = None

    def __init__(self, gui):
        super().__init__(gui)
        self.scene_init()

    def scene_init(self):
        self._random_force = RandomForce(self._player)
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
        if self._player.ready:

            self._random_force.update()

            # for obj in self.__scene_objects:
            #     self._random_force.in_collision(obj)
            #     obj.in_collision(obj, *self.__scene_objects, *self._players)
            #     obj.update()

            for player in self._players:
                # self._random_force.in_collision(player)
                player.in_collision(player, *self._players, *self.__scene_objects)
                player.update()

    def render(self, qpainter):
        if self._player.ready:

            for player in self._players:
                player.render(qpainter)

            for obj in self.__scene_objects:
                obj.render(qpainter)

            self._random_force.render(qpainter)
