class shape :
    def __init__(self,color,name) :
        self.__name =name
        self.__color=color
    def getColor(self):
        return self.__color
    def setColor(self,color):
        return self.__color== color
    def calcArea(self):
        pass
    