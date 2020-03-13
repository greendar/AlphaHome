def dot(aVec, bVec):
    return aVec.vx * bVec.vx + aVec.vy * bVec.vy + aVec.vz * bVec.vz

def cross(aVec, bVec):
    cX = aVec.vy * bVec.vz - aVec.vz * bVec.vy
    cY = aVec.vz * bVec.vx - aVec.vx * bVec.vz
    cZ = aVec.vx * bVec.vy - aVec.vy * bVec.vx
    c = Vector(cX, cY, cZ)
    return c

class Vector:
    def __init__(self, vx, vy, vz = 0):
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def __str__(self):
        if self.vz == 0:
            return f"[{self.vx}, {self.vy}]"
        else:
            return f"[{self.vx}, {self.vy}, {self.vz}]"

    def __add__(self, other):
        cX = self.vx + other.vx
        cY = self.vy + other.vy
        cZ = self.vz + other.vz
        c = Vector(cX, cY, cZ)
        return c

    def mag(self):
        return (self.vx**2 + self.vy**2 +self.vz**2)**0.5

class Line:
    def __init__(self, posVec, dirVec):
        self.posVec = posVec
        self.dirVec = dirVec

    def __str__(self):
        return f"R = {self.posVec} + t * {self.dirVec}"

class Plane:
    def __init__(self, posVec, dirVec1, dirVec2):
        self.posVec = posVec
        self.dirVec1 = dirVec1
        self.dirVec2 = dirVec2

    def __str__(self):
        return f"R = {self.posVec} + s * {self.dirVec1} + t * {self.dirVec2}"
