from module1 import shape
class Rectangle(shape):
    def __init__(self, name, color, length, width):
        super().__init__(name, color)
        self.length = length
        self.width = width

    def calcArea(self):
        return self.length * self.width
