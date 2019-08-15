#coding utf8
import threading,time

count = 0
lock = threading.Lock()

class MyThread(threading.Thread):
    def __init__(self,lock,threadName):
        super(MyThread,self).__init__(name = threadName)
        self.lock = lock

    def run(self):
        global count
        self.lock.acquire()

        for i in range(5):
            count = count + 1
            time.sleep(0.3)
            print(self.getName(),count)

        self.lock.release()

for i in range(3):
    MyThread(lock,"MyThreadName:" + str(i)).start()