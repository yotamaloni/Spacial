from geometry.vector import Vec3
from geometry.plane import Plane

class Surface:
    def __init__(self, nodes):
        self.nodes = nodes
        self.plane = Plane(
            nodes[0].as_np(),
            nodes[1].as_np(),
            nodes[2].as_np()
        )
