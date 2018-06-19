class Point3D(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self): # to print in a different style, this is over-riding repr
        print str((self.x,self.y,self.z))

myPoint = Point3D(1,2,3)
myPoint.__repr__()