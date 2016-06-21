#而threading模块支持守护线程，守护线程一般是一个等待客户请求的服务器，
# 如果没有客户提出请求它就在那等着，如果设定一个线程为守护线程，就表示这
# 个线程是不重要的，在进程退出的时候，不用等待这个线程退出。如果主线程退出
# 不用等待那些子线程完成，那就设定这些线程的daemon属性，即在线程thread.start()
# 开始前，调用setDaemon()函数设定线程的daemon标志(thread.setDaemon(True))
# 就表示这个线程“不重要”。如果想要等待子线程完成再退出，那就什么都不用做或者显式地
# 调用thread.setDaemon(False)以保证其daemon标志为False，可以调用thread.isDaemon()
# 函数来判断其daemon标志的值。新的子线程会继承其父线程的daemon标志，整个Python会在所有的非
# 守护线程退出后才会结束，即进程中没有非守护线程存在的时候才结束。
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
    for i in range(0, 5):
        t = MyThread("thread_" + str(i))
        t.run()
        # 这里的 t 可同时处理多个线程，即 t 为线程句柄，重新赋值不影响线程。
        # 这里奇怪的是，运行 t.run() 时，不会再执行其他线程。虽不明，还是用 start() 吧。
        # 暂且理解为 start() 是非阻塞并行的，而 run 是阻塞的。

if __name__=='__main__':
    # test()
    t = MyThread("thread_" + str(1))
    t.setDaemon(True)
    t.run()
    print("Main Thread is over")
