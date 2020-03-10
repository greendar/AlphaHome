class Vector:
    def __init__(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def show(self):
        print(f"[{self.vx}, {self.vy}]")

    def mag(self):
        return (self.vx**2 + self.vy**2)**0.5


"""
a = Vector(3, 4)
b = Vector(5, 6)

a.show()
b.show()


"""
