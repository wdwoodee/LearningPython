#-*- coding:utf-8 -*-
__author__ = ''

class ImportForAndFrom():   #类
    def __init__(self,a = 0):  #构造函数
        self.a = a
    def print_message1(self):   #类方法
        print("类方法调用：传参，使用构造函数的方式")
        print(self.a)
        print ()
    def print_message2(self):   #类方法
        print("类方法调用：无参")
        print("This is a test for import!")
        print()

def print_line(arg):  #函数
    print(arg)

test = 200
# s1 = ImportForAndFrom()
# s2 = ImportForAndFrom(1000)
# s2.print_message1()
# s1.print_message2()
# print_line(20000)

print("Import_from __name__:{0}".format(__name__))

if __name__ == "__main__":
    s1 = ImportForAndFrom()
    s2 = ImportForAndFrom(1000)
    s2.print_message1()
    s1.print_message2()
    print_line(20000)
