#__author__ = 'chubby_superman'
#_*_coding=utf-8 _*
import threading
import time

#定义一个方法
def tr(a,b):
    print(a,b)
    pass

class Mythread(threading.Thread):
    #使用继承实现多线程
    def __init__(self,func,*args):
        threading.Thread.__init__(self)
        self.func=func  #功能名
        self.args=args  #功能所需参数
    #初始化父类  threading.Thread
    def run(self):
        lock = threading.Lock()
        if lock.acquire():
            self.func()   #调用run方法，实现功能的多线程
            print(self.name,time.ctime())
            lock.release()
    #给需要实现多线程的功能 加锁。注意：run方法为重写父类threading.Thread的run方法，函数名不得改变，且此方法必须有。
if __name__=="__main__":
    thread_list=[]
    lock = threading.Lock()
    for i in range(5):  #需要开启多少线程，range中的数字填多少，此处需要5个
        t = thread_list.append(Mythread(tr,1,2))
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
