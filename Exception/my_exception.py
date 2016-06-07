class BadNumberError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def inputAge():
        try:
            age = int(input("Input your age:"))
            if (age>100 or age<18):
                raise BadNumberError('out of range')#自定义异常
            print(age)
        except BadNumberError as err:
            #print("自定义异常",err)
            print("自定义异常{0}".format(err))
        # except BadNumberError:
        #     print("自定义异常",err)
        #     print("自定义异常{0}".format(err))


if __name__ == "__main__":
    inputAge()




