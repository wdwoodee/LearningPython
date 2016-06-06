__author__ = 'Administrator'
previous = {0:0, 1:1}
def fibonacci(n):
    if n in previous:
        print("a:{0}".format(previous[n]))
        print("a:{0}".format(previous))
        return previous[n]
    else:
        newVaule = fibonacci(n - 1) + fibonacci(n - 2)
        previous[n] = newVaule
        print("b:{0}".format(previous[n]))
        print("b:{0}".format(previous))
        return newVaule
if __name__ == "__main__":
    # print(fibonacci(0))
    # print(fibonacci(1))
    # print(fibonacci(2))
    # print(fibonacci(3))
    # print(fibonacci(4))
    # print(fibonacci(5))
    # print(fibonacci(6))
    fibonacci(4)