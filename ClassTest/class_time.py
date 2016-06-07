# -*- coding: utf-8 -*-
#构造函数的实现方式


class Time:
    def __init__(self, hours = 0, minutes = 0, seconds = 0): #构造函数，对参数型对象进行初始化，如：a=Time(1,1,1)
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def printTime(self): #类方法，打印时间
        print (str(self.hours) + ":" + \
              str(self.minutes) + ":" + \
              str(self.seconds))



    def increment(self, seconds):  #类方法，一定的时间，加上秒后打印新的时间
         self.seconds = seconds + self.seconds
         while self.seconds>=60:
            self.seconds = self.seconds - 60
            self.minutes = self.minutes + 1
         while self.minutes>=60:
            self.minutes = self.minutes - 60
            self.hours = self.hours + 1
         print (str(self.hours) + ":" + \
               str(self.minutes) + ":" + \
               str(self.seconds))


    def after(self, time):  #类方法，判断时间的先后
            if self.hours > time.hours:
                return 1
            elif self.hours < time.hours:
                return 0
            else:
                if self.minutes > time.minutes:
                    return 1
                elif self.minutes < time.minutes:
                    return 0
                else:
                    if self.seconds > time.seconds:
                        return 1
                    elif self.seconds < time.seconds:
                        return 0
                    else:
                        return 3

if __name__ == "__main__":

    time = Time(12,12,12)  #使用构造函数，直接传递参数进行初始化
    time.printTime()

    t1 = Time()    #无参，打印默认值
    t1.printTime()

    after = Time()
    after.hours = 11   #不使用构造函数的初始化方式
    after.minutes = 19
    after.seconds = 11

    now = Time()
    now.hours = 10  #不使用构造函数的初始化方式
    now.minutes = 30
    now.seconds = 10

    now.printTime()
    now.increment(100)
    after.printTime()
    if now.after(after) < 1:
        print("now time is smaller than after time")


    #函数的实现方式
    #class Time:
     #   pass

    #def printTime(time):
     #    print str(time.hours) + ":" + \
      #         str(time.minutes) + ":" + \
       #        str(time.seconds)


    #now = Time()
    #now.hours = 10
    #now.minutes = 30
    #now.seconds = 10
    #printTime(now)

