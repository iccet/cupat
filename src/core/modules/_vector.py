from typing import List, TypeVar, Iterator, Iterable
import math

T = TypeVar('T', int, float, complex)
Vector = Iterable[List[T]]


# noinspection PyTypeChecker
class Vector:
    """ Vector[T] methods implementation
    translation :
        Vector[T](self) on Vector[T](other)
         __add__(), __iadd__() : with '+' sign
         __sub__(), __isub__() : with '-' sign
    rotation :
        Vector[T](self) by matrix
         __matmul__(), __imatmul__(), rotate() 
    """
    __null_vector = None  # alias for zero abs vector
    _carr: List[T] = None  # coordinates array
    _sup_arr: List[T] = None  # support array for calc angle between vectors in range(-pi, +pi)

    @staticmethod
    def _sum(x, y):
        return x + y

    @staticmethod
    def _sub(x, y):
        return x - y

    @staticmethod
    def _mul(x, y):
        return x * y

    @staticmethod
    def _pow(x, y):
        return x ** y

    @staticmethod
    def _div(x, y):
        return x / y

    def __sup_vector_angle(self):
        return math.atan2(*self)

    @staticmethod
    def angle_between_vectors(v1, v2=None, default_range: bool = True) -> float:
        """ Return angle between vector in
        default_range: [0, 180]
        or
        not default_range: [-180, 180]
        """
        if v2 is None:
            v2 = Vector._sup_arr
        if default_range:
            return -(v1.__sup_vector_angle() - v2.__sup_vector_angle())
        else:
            try:
                return math.acos(sum(v1 * v2) / (abs(v1) * abs(v2)))
            except ZeroDivisionError:
                return 0

    def __init__(self, *args, _sup_arr: list = (1, 0)) -> Vector[T]:
        self._carr = []
        try:
            for i in range(len(args)):
                self._carr += [*args[i]]
        except TypeError:
            self._carr = list(args)
        self._sup_arr = _sup_arr
        self.__null_vector = [0 for _ in self._carr]

    def __str__(self):
        return " ".join(str(i) for i in self)

    def __getitem__(self, item):
        return self._carr[item]

    def __setitem__(self, key, value):
        self._carr[key] = value

    def __iter__(self) -> Iterator[T]:
        for i in self._carr:
            yield i

    def __reversed__(self):
        for i in range(len(self._carr), 0, -1):
            yield self._carr[i]

    def __len__(self) -> int:
        return len(self._carr)

    def __neg__(self) -> Vector[T]:
        return Vector(-i for i in self)

    def __pos__(self) -> Vector[T]:
        return self

    @classmethod
    def is_collinear(cls, self, other, digits=1) -> bool:
        _len = len(self)
        try:
            _k = round(self[0], digits) / round(other[0], digits)
        except ZeroDivisionError:
            return True
        for i in range(1, _len):
            _self_r = round(self[i], digits)
            _other_r = round(other[i], digits)
            if _self_r and not _other_r:
                return False
            if not _self_r or not _other_r:
                continue
            if _self_r / _other_r != _k:
                return False
        return True

    @classmethod
    def is_eq_abs(cls, self, other, digits=1) -> bool:
        """ Checking for equal abs of
        Vector[T]s :
            { self }, { other },
        with
        accuracy :
            { digits } signs.
        """
        _self_abs = round(abs(self), digits)
        if _self_abs != round(abs(other), digits):
            return False
        return True

    def to_list(self) -> list:
        return list(self)

    def __eq__(self, other) -> bool:
        if self.is_collinear(self, other):
            return self.is_eq_abs(self, other)
        return False

    def __ne__(self, other) -> bool:
        return not (self == other)

    def __le__(self, other) -> bool:
        if self.is_collinear(self, other):
            return abs(self) <= abs(other)
        return False

    def __ge__(self, other) -> bool:
        if self.is_collinear(self, other):
            return abs(self) >= abs(other)
        return False

    def __lt__(self, other) -> bool:
        if self.is_collinear(self, other):
            return abs(self) < abs(other)
        return False

    def __gt__(self, other) -> bool:
        if self.is_collinear(self, other):
            return abs(self) > abs(other)
        return False

    def __abs__(self) -> float:
        return math.sqrt(sum(map(self._mul, self, self)))

    def __add__(self, other: Vector[T]) -> Vector[T]:
        return Vector(*map(self._sum, self, other))

    def __iadd__(self, other: Vector[T]) -> Vector[T]:
        self._carr = list(map(self._sum, self, other))
        return self

    def __sub__(self, other: Vector[T]) -> Vector[T]:
        return Vector(*map(self._sub, self, other))

    def __isub__(self, other: Vector[T]) -> Vector[T]:
        self._carr = list(map(self._sub, self, other))
        return self

    def __pow__(self, power, modulo=None):
        return Vector(*map(lambda x: x ** power, self))

    def __ipow__(self, power, modulo=None):
        self._carr = list(map(lambda x: x ** power, self))
        return self

    def __mul__(self, other) -> Vector[T]:
        """ Overloaded multiplication """
        if isinstance(other, int) or isinstance(other, float):
            return Vector(map(lambda x: x * other, self))
        else:
            return Vector(map(self._mul, self, other))

    def __imul__(self, other) -> Vector[T]:
        self = self * other
        return self

    def __truediv__(self, other) -> Vector[T]:
        """ Overloaded division """
        if isinstance(other, int) or isinstance(other, float):
            return Vector(*map(lambda x: x / other, self))
        else:
            return Vector(*map(self._div, self, other))

    def __itruediv__(self, other) -> Vector[T]:
        self = self / other
        return self

    def copy(self) -> Vector[T]:
        _ca = list(self._carr).copy()
        return Vector(*_ca)

    def __copy__(self) -> Vector[T]:
        return self.copy()

    def __matmul__(self, matrix: list):
        """ Multiplying vector by matrix """
        try:
            matrix = list(matrix)
        except Exception:
            raise Exception("Cant convert matrix to list.")
        m = len(self)
        n = len(matrix)
        if m != n:
            raise Exception("Multiply vector error: Incompatible dimensions.")
        return Vector((sum(self[p] * matrix[p][i] for p in range(n)) for i in range(m)))

    def __imatmul__(self, matrix):
        self = self @ matrix
        return self

    @classmethod
    def make_vector(cls, v_begin: Vector[T], v_end=None) -> Vector[T]:
        """ Create Vector[T] from points:
        v_begin - begin point, or Vector[T] out zero coordinates
        v_end - end point, or Vector[T] out zero coordinates.
        """
        if v_end is None:
            v_end = Vector([0, 0])
        return cls(*map(Vector._sub, v_end, v_begin))

    def normalized(self, k: float = 1) -> Vector[T]:
        """ Return new normalized of instance self Vector[T]"""
        _abs = abs(self)
        if _abs:
            return Vector(k * i / _abs for i in self._carr)
        else:
            return Vector(*self.__null_vector)

    def normalize(self, k: float = 1) -> None:
        """ Conversion of a self Vector[T]
        into a Vector[T] in the same direction with a length == k.
        """
        _abs = abs(self)
        if _abs:
            self._carr = [k * i / _abs for i in self._carr]
        else:
            self._carr = [0 for _ in self._carr]
        return self

    def get_angle(self, other) -> float:
        return self.angle_between_vectors(self, other)

    def rotate(self, a: float, _v: Vector[T] = None) -> Vector[T]:
        """ 2d rotate
        a: angle (rad),
        p: rotation point
        
        Maybe override for more dimensional vector rotate
        """
        if _v is None:
            _v = Vector(0, 0)
        _len = len(self)
        if _len > 1:
            c = math.cos(a)
            s = math.sin(a)
            self -= _v
            self @= [[c, -s],
                     [s, c]]
            self += _v
        else:
            raise Exception(f"Cant rotate {_len}-dimensional Vector[T].")
        return self
