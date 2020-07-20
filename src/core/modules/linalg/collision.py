from .vector import Vector
from .matrix import SqMatrix
from abc import ABC, abstractmethod


class collisionhandler(ABC):
    _func = None

    def __init__(self, function):
        self._func = function

    def __call__(self, *objects):
        _this = objects[0]
        for i in range(1, len(objects)):
            obj = objects[i]
            if id(_this) == id(obj):
                continue
            self.box_collide(_this, obj)
        self._func(_this)

    def box_collide(self, this, obj):
        _ts = this.collision_box[2:]  # this collision box size
        _tc = this.collision_box[:2]  # this collision box coord
        _os = obj.collision_box[2:]  # obj collision box size
        _oc = obj.collision_box[:2]  # obj collision box coord

        tx0, ty0 = _tc
        ox0, oy0, = _oc
        tx, ty = Vector(_ts) + Vector(_tc)
        ox, oy = Vector(_os) + Vector(_oc)

        if tx < ox0:
            return
        elif tx0 > ox:
            return
        elif oy < ty0:
            return
        elif oy0 > ty:
            return
        self.shape_collision(this, obj)

    @staticmethod
    @abstractmethod
    def shape_collision(this, obj):
        pass


class Collision:
    class Elastic(collisionhandler):

        @staticmethod
        def shape_collision(this, obj):
            _tc = this.collision
            _oc = obj.collision
            _tcm = this.center_mass
            _ocm = obj.center_mass
            _ltc = len(_tc)
            _loc = len(_oc)

            tvec = sorted((abs(_ocm - _tc[i]), i) for i in range(_ltc))[:2]
            ovec = sorted((abs(_tcm - _oc[i]), i) for i in range(_loc))[:2]
            _a = Vector.angle_between_vectors(_tc[tvec[1][1]] - _tc[tvec[0][1]], _oc[ovec[1][1]] - _oc[ovec[0][1]])
            this.speed.value = this.speed.value.rotate(_a)

    class NonElastic(collisionhandler):
        @staticmethod
        def shape_collision(this, obj):
            pass
