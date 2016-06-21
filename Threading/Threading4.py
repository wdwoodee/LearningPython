# 子类化Thread类，MyThread子类的构造函数一定要先调用基类的构造函数，
# 特殊函数__call__()在子类中，名字要改为run()。在 MyThread类中，
# 加入一些用于调试的输出信息，把代码保存到myThread模块中，并导入这个类。
# 除使用apply()函数来运行这些函数之外，还可以把结果保存到实现的self.res
# 属性中，并创建一个新的函数getResult()来得到结果。
import threading
from time import sleep, ctime 

loops = [ 4, 2 ]
class MyThread(threading.Thread):
   def __init__(self, func, args, name=''):
      threading.Thread.__init__(self)
      self.name = name
      self.func = func
      self.args = args

   def getResult(self):
      return self.res

   def run(self):
      print ('starting', self.name, 'at:', ctime())
      self.res = self.func(*self.args)
      print (self.name, 'finished at:', ctime())

def loop(nloop, nsec):
   print ('start loop', nloop, 'at:', ctime())
   sleep(nsec)
   print ('loop', nloop, 'done at:', ctime())
  
def main(): 
   print ('starting at:', ctime())
   threads = []
   nloops = range(len(loops))
  
   for i in nloops:
      t = MyThread(loop, (i, loops[i]),
                 loop.__name__)
      threads.append(t)
  
   for i in nloops:
      threads[i].start()
  
   for i in nloops:
      threads[i].join()
  
   print ('all DONE at:', ctime())
  
if __name__ == '__main__': 
  main()