__author__ = ''

# import import_from
# import文件，会把所有的类和方法都import进来

# from import_from import ImportForAndFrom
# from import_from import print_line

from import_from import *

print("import __name__:{0}".format(__name__))

if __name__ == "__main__":
    # s1 = import_from.ImportForAndFrom(2)  #直接import文件时，创建对象，必须要加文件名，配合import文件时使用
    # s1 = ImportForAndFrom(2)

    s1 = ImportForAndFrom(test)  #也可以通过from import_from import * 把变量也传过来
    s1.print_message1()
    s2 = ImportForAndFrom()
    # s2 = import_from.ImportForAndFrom()  #直接import文件时，创建对象，必须要加文件名，配合import文件时使用
    print (s1)  #打印对象
    print (s2)
    s2.print_message2()
    # import_from.print_line(4)  #直接import文件时，调用方法，要以（文件名.文件中的方法名）的格式调用文件中的方法
    print_line(4)
