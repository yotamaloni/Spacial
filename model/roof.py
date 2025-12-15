from model.surface import Surface
from geometry.vector import Vec3

class Roof:
    def __init__(self, json_data):
        self.surfaces = []
        self._parse(json_data)

    def _parse(self, data):
        for roof in data["roofs"]:
            for s in roof["surfaces"]:
                nodes = []
                for n in s["polygon"]["nodes"]:
                    p = n["point"]
                    nodes.append(Vec3(p["x"], p["y"], p["z"]))
                self.surfaces.append(Surface(nodes))

    def x_bounds(self):
        xs = []
        for s in self.surfaces:
            for n in s.nodes:
                xs.append(n.x)
        return min(xs), max(xs)
