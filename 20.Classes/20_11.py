#  20_11

class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "(%s, %s, %s)" % (str(self.x), str(self.y), str(self.z))

my_point = Point3D(1, 2, 3)
print my_point