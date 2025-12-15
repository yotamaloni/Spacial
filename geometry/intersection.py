from config import EPSILON
from geometry.vector import Vec3

def intersect_segment_with_x(p1: Vec3, p2: Vec3, x_value: float):
    """
    Intersect line segment P1-P2 with plane X = constant
    """
    x1, x2 = p1.x, p2.x

    if (x1 - x_value) * (x2 - x_value) > 0:
        return None

    if abs(x2 - x1) < EPSILON:
        return None

    t = (x_value - x1) / (x2 - x1)
    if 0.0 <= t <= 1.0:
        point = p1.v + t * (p2.v - p1.v)
        return Vec3(*point)

    return None
