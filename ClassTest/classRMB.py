class RMB:
    def __init__(self,sum = 0.0):
        self.sum = sum
    def __str__(self):
        return str(self.sum)
    def __add__(self,other): #重定义加法运算符
        return RMB(self.sum + other.sum)
    def __sub__(self,other): #重定义减法运算符
        return RMB(self.sum - other.sum)
    def printRMB(self):   #定义类方法，打印当前值
        print (self.sum)

if __name__ == "__main__":
    a = RMB(456)
    b = RMB(123.123)
    print("a = %s" %a) #使用构造函数__str__返回值，打印a的值，这倒是一个方法，值得借鉴
    print("a = %s" %b)
    print("print value a and b")
    print(a)  #直接打印，估计使用的__str__返回值
    print(b)
    a.printRMB()  #调用类打印方法
    b.printRMB()
    print()
    print("print a + b")
    print (a + b) #运算符重定义
    print()
    print("print a - b")
    print (a - b)
    print()
    (a + b).printRMB()  #调用类方法
    (a - b).printRMB()
    print(a.__add__(b),a + b)
    print(a.__sub__(b),a - b)

