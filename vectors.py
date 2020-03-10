def dot(aVec, bVec):
    return aVec.vx * bVec.vx + aVec.vy * bVec.vy + aVec.vz * bVec.vz

def cross(aVec, bVec):
    cX = aVec.vy * bVec.vz - aVec.vz - bVec.vy
    cY = aVec.vz * bVec.vx - aVec.vx - bVec.vz
    cZ = aVec.vx * bVec.vy - aVec.vy - bVec.vx
    c = Vector(cX, cY, cZ)
    return c
    
class Vector:
    def __init__(self, vx, vy, vz = 0):
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def __str__(self):
        if self.vz == 0:
            print(f"[{self.vx}, {self.vy}]")
        else:
            print(f"[{self.vx}, {self.vy}, {self.vz}]")

    def mag(self):
        return (self.vx**2 + self.vy**2 +self.vz**2)**0.5


"""
a = Vector(3, 4)
b = Vector(5, 6)

a.show()
b.show()


"""
