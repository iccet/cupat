import math
from vector import Vector


def circumscribed_radius(obj):
    x_component = tuple(Vector.component(obj.collision, 0))
    y_component = tuple(Vector.component(obj.collision, 1))
    min_x = min(x_component)
    min_y = min(y_component)
    max_x = max(x_component)
    max_y = max(y_component)

    return abs(Vector(max_x, max_y) - Vector(min_x, min_y)) / 2


def regular(radius: float, n: int = 4) -> list:
    """ Generate regular polygon
    @param radius: float
    @param n: int
    @return: List of points enclosing an @n-compound box primitive around the @collision_base
    @rtype: list
    """
    if not isinstance(n, int) or n < 2:
        raise TypeError

    step = 2 * math.pi / n
    angles = [i * step for i in range(n)]
    return [Vector(math.cos(angle), math.sin(angle)) * radius for angle in angles]
