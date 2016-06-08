__author__ = 'dwang'

class Person():
    def __init__(self,
                 name = None,
                 age = 1,
                 sex = "men"):
        self.name = name
        self.age = age
        self.sex = sex

    def displayInfo(self):
        print ("name:%-20s" % self.name)
        print ("age:%-20d" % self.age)
        print ("sex:%-20s" % self.sex)

class Student(Person):  #继承person类
    def __init__(self,
                 name = None,
                 age = 1,
                 sex = "men",
                 grade = 0):
        Person.__init__(self, name, age, sex)  #使用父类进行初始化
        self.grade = grade

    def displayInfo(self):
        Person.displayInfo(self)      #调用父类的打印方法
        print("grade:%-20d" % self.grade)


if __name__ == "__main__":
    p = Person("xiaoming", 20, "men")
    st = Student("xiaowang", 22, "female", 15)
    p.displayInfo()
    print() #打印空行
    st.displayInfo()