from module2 import circle
from module3 import Square
from module4 import Rectangle

c = circle("Circle", "Red", 5)
print("Area of Circle:", c.calcArea())

s = Square("Square", "Blue", 5)
print("Area of Square:", s.calcArea())

r = Rectangle("Rectangle", "Green", 5, 5)
print("Area of Rectangle:", r.calcArea())
