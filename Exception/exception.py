while 1:
    try:
        x = int(input("Input a number:"))
        y = int(input("Input a number:"))
        z = x/y
    except ValueError as ev:
        '''第一个参数是异常的类型，第二
个参数用于接收异常发生时生成的值，异常是否有这个参数及参数的类型
如何，由异常的类型决定。'''
        print("That is a invalid number", ev)

    except ZeroDivisionError as ez:
        print("divisor is zero", ez)
    except:
        print("Unexcepted error.")
        raise
    else:
        print("There is no error")
        print(x, "/", y, "=", x/y)
        break

    '''最后一个except语句表示当有异常发生，但不是前面定义的两种类
型，就执行这条语句。用这样的except 语句要小心，理由是你很可能把
一个应该注意的的程序错误隐藏了。为了防止这种情况的发生，我们用
了raise语句，将异常抛出。'''



