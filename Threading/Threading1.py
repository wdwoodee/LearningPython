import threading
import time
class MyThread(threading.Thread):
    def __init__(self,thread_name = None):
        threading.Thread.__init__(self)
        self.setName(thread_name)
    def run(self):
        print("This is thread" + self.getName())
        for i in range(5):
            time.sleep(1)
            print(str(i))
        print(self.getName()+" is over")
def test():
    for i in range(0, 3):
        t = MyThread("thread_" + str(i))
        t.start()

if __name__=='__main__':
    test()
    # t = MyThread("thread_" + str(1))
    # t.start()
