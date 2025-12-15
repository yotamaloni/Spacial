import numpy as np

class Vec3:
    def __init__(self, x, y, z):
        self.v = np.array([x, y, z], dtype=float)

    @property
    def x(self): return self.v[0]
    @property
    def y(self): return self.v[1]
    @property
    def z(self): return self.v[2]

    def __add__(self, other):
        return Vec3(*(self.v + other.v))

    def __sub__(self, other):
        return Vec3(*(self.v - other.v))

    def scale(self, t):
        return Vec3(*(self.v * t))

    def as_np(self):
        return self.v
