from module1 import shape
class circle (shape):
    def __init__ (self,name,color,raduis):
        super().__init__(name,color)
        self.raduis=raduis
    def calcArea(self):
        return 3.14 * self.raduis ** 2