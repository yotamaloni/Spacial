from geometry.intersection import intersect_segment_with_x

class Truss:
    def __init__(self, x_position_cm):
        self.x = x_position_cm
        self.points = []

    def add_point(self, p):
        self.points.append(p)

    def valid(self):
        return len(self.points) >= 3


class TrussGenerator:
    def __init__(self, roof, spacing_cm):
        self.roof = roof
        self.spacing = spacing_cm

    def generate(self):
        x_min, x_max = self.roof.x_bounds()
        trusses = []

        x = x_min
        while x <= x_max:
            truss = Truss(x)

            for surface in self.roof.surfaces:
                nodes = surface.nodes
                for i in range(len(nodes)):
                    p1 = nodes[i]
                    p2 = nodes[(i + 1) % len(nodes)]
                    ip = intersect_segment_with_x(p1, p2, x)
                    if ip:
                        truss.add_point(ip)

            if truss.valid():
                trusses.append(truss)

            x += self.spacing

        return trusses
