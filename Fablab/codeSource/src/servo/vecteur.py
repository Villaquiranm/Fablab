class Vecteur:
    x = 0
    y = 0
    z = 0
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def deplaceX(self,dx):
        self.x += dx

    def deplaceY(self,dy):
        self.y += dy

    def deplaceZ(self,dz):
            self.z += dz

    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y

    def setZ(self,z):
        self.z = z
