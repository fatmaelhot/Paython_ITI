from module1 import shape
class Square(shape):
    def __init__(self, name, color, side):
        super().__init__(name, color)
        self.side = side

    def calcArea(self):
        return self.side ** 2
