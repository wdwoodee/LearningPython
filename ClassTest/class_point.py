#-*- coding:utf-8 -*-
#通过长方形的左下角，找到长方形的右上角

class Point: #定义点的类
    pass

class Rectangle: #定义长方形的类
    pass

def findUpperRight(rectangle):  #定义函数，找到长方形的右上角
    p = Point()
    p.x = rectangle.width + rectangle.corner.x
    p.y = rectangle.height + rectangle.corner.y
    return p


if __name__ == "__main__":
    r = Rectangle()
    r.width = 50.0
    r.height = 70.0
    r.corner = Point()
    r.corner.x = 10
    r.corner.y = 5

    upRight = findUpperRight(r)
    print("The right corner of the rectangle is:")
    print ('(' + str(upRight.x) + ',' +str(upRight.y) + ')') #打印右上角
    print("The square of rectangle is:")
    print ((upRight.x - 10) * (upRight.y - 5))   #打印长方形的面积
    print (r.width * r.height)
    
