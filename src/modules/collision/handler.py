from vector import Vector
from abc import ABC, abstractmethod
import operator


class AbstractHandler(ABC):
    _func = None

    def __init__(self, function):
        self._func = function

    def __call__(self, *objects):
        this = objects[0]
        for i in range(1, len(objects)):
            other = objects[i]
            if id(this) == id(other):
                continue
            if self.box_collide(this, other):
                self.shape_collision(this, other)
        self._func(this)

    @staticmethod
    def box_collide(this, other):
        _ts = this.collision_box[2:]
        _tc = this.collision_box[:2]
        _os = other.collision_box[2:]
        _oc = other.collision_box[:2]

        tx0, ty0 = _tc
        ox0, oy0, = _oc
        tx, ty = Vector(_ts) + Vector(_tc)
        ox, oy = Vector(_os) + Vector(_oc)
        # tx, ty, ox, oy = [sum(i) for i in zip(this.collision_box, other.collision_box)]

        if tx < ox0 or tx0 > ox or oy < ty0 or oy0 > ty:
            return False
        return True

    @staticmethod
    @abstractmethod
    def shape_collision(this, obj):
        pass


class ElasticHandler(AbstractHandler):

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


class NonElasticHandler(AbstractHandler):
    @staticmethod
    def shape_collision(this, obj):
        pass
