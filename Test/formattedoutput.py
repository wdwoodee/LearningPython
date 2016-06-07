__author__ = 'dwang'
for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))
    # print(repr(x).rjust(2), repr(x*x).rjust(3), end = " ")
    # print(repr(x*x*x).rjust(4))

for x in range(1,11):
    # print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))
    print(repr(x).rjust(2), repr(x*x).rjust(3), end = " ")
    print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    print("{0:2d} {1:3d} {2:4d}".format(x, x*x, x*x*x))

name = "xiaoming"
age = 20
print("My name is:%s"%name)
print("My name is %s, age is %d"%(name,age))  #旧格式，%前无逗号
print("My name is:{}".format(name))
print("My name is {0}, age is {1}".format(name, age))#新格式

import math
print("The value of PI is approximately %5.3f."%math.pi) #旧格式
print("The value of PI is approximately {0:5.3f}.".format(math.pi)) #新格式

print("Name is:%10s Age:%8d Height:%8.2f"%("Avaiad",25,1.83)) #旧格式
print("Name is:%-10s Age:%-8d Height:%-8.2f"%("Avaiad",25,1.83)) #旧格式
print("Name is:{0:>10s} Age:{1:>8d} Height:{2:>8.2f}".format("Avaiad",25,1.83)) #新格式
print("Name is:{0:<10s} Age:{1:<8d} Height:{2:<8.2f}".format("Avaiad",25,1.83)) #新格式
print("Name is:{0:^10s} Age:{1:^8d} Height:{2:^8.2f}".format("Avaiad",25,1.83)) #新格式

# format
# < （默认）左对齐
# > 右对齐
# ^ 中间对齐
# = （只用于数字）在小数点后进行补齐