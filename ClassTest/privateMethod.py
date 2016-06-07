__author__ = 'dwang'

import math
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

class Line:
    def __init__(self, p1 = Point(), p2 = Point()):
        self.__p1 = p1   #private variable
        self.__p2 = p2
    def __str__(self):
        return str(self.__p1) + str(self.__p2)#不明白是干啥的
    def __distance(self): #private method
        tx = math.pow(self.__p1.x, 2) + math.pow(self.__p2.x, 2) - 2 * p1.x * p2.x
        ty = math.pow(self.__p1.y, 2) + math.pow(self.__p2.y, 2) - 2 * p1.y * p2.y
        return math.sqrt(tx + ty)
    def length(self):
        print (self.__distance())

if __name__ == "__main__":
    p1 = Point(1,2)
    print("point p1:")
    print(p1)
    p2 = Point(4,6)
    print("point p2:")
    print(p2)
    line = Line(p1,p2)
    line.length()