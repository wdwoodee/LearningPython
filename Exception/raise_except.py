# -*- coding: utf-8 -*-
from my_exception import BadNumberError
#import my_eception
__author__ = 'dwang'
def raise_except():
    age = int(input("Input your age:"))
    if (age > 100 or age < 0):
        raise BadNumberError("out of range")
    print("Your input is right:your age is %d" %age)

if __name__ == "__main__":
    raise_except()
''' try:
    raise MyError #自己抛出一个异常
except MyError:
    print ('a error')

raise ValueError(’invalid argument’)
捕捉到的内容为:

type = VauleError
message = invalid argument'''