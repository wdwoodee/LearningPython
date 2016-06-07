class Time:
    def __init__(self,hours = 0,minutes = 0,seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def printTime(self):
         print (str(self.hours) + ":" + \
		      str(self.minutes) + ":" + \
		      str(self.seconds))

if __name__ == "__main__":
    now = Time(12,12,12)
    now.printTime()
    now2 = Time()
    now2.printTime()
    now3 = Time(23)
    now3.printTime()
    now4 = Time(23,12)
    now4.printTime()
    now5 = Time(seconds = 22,hours = 12)
    now5.printTime()
