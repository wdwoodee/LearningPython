#-*- coding:utf-8 -*-
try:
    raise NameError('Hi There!')
except NameError:
    print('An exception flew by!')
    raise



'''
要抛出的异常由raise的唯一参数标识。它必需是一个异常实例或异常类（继承自
Exception的类）。
如果你需要明确一个异常是否抛出，但不想处理它，raise语句可以让你很简单的重新抛
出该异常:
'''