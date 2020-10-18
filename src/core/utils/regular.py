import math
from vector import Vector


def square_mask(obj):
    x_component = tuple(Vector.component(obj.collision, 0))
    y_component = tuple(Vector.component(obj.collision, 1))
    return min(x_component), min(y_component), max(x_component), max(y_component)


def circumscribed_radius(obj):
    min_x, min_y, max_x, max_y = square_mask(obj)
    return abs(Vector(max_x, max_y) - Vector(min_x, min_y)) / 2


def regular(radius: float, n: int = 4) -> list:
    """ Generate regular polygon
    @param radius: float
    @param n: int
    @return: List of points enclosing an @n-compound box primitive around the @collision_base
    @rtype: list
    """
    if not isinstance(n, int) or n < 3:
        raise TypeError

    step = 2 * math.pi / n
    angles = [i * step for i in range(n)]
    return [Vector(math.cos(angle), math.sin(angle)) * radius for angle in angles]
