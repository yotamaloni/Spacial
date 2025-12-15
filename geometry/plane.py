import numpy as np

class Plane:
    def __init__(self, p1, p2, p3):
        v1 = p2 - p1
        v2 = p3 - p1
        normal = np.cross(v1, v2)
        normal = normal / np.linalg.norm(normal)

        self.A, self.B, self.C = normal
        self.D = -np.dot(normal, p1)

    def height_at(self, x, y):
        """
        Solve Ax + By + Cz + D = 0 for Z
        """
        if abs(self.C) < 1e-6:
            return None
        return (-self.A * x - self.B * y - self.D) / self.C
