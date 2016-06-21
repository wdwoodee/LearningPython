import threading
import time
class MyThread(threading.Thread):
  def __init__(self, thread_name = None):
    threading.Thread.__init__(self)
    self.setName(thread_name)
  def run(self):
    threadLock.acquire()
    #获得锁之后再运行
    print ("This is thread " + self.getName())
    for i in range(3):
      time.sleep(1)
      print (str(i))
    print (self.getName() + " is over")
    threadLock.release()
    #释放锁
if __name__ == '__main__':
  threadLock = threading.Lock()
  #设置全局锁
  thread1 = MyThread('Thread_1')
  thread2 = MyThread('Thread_2')
  thread1.start()
  thread2.start()