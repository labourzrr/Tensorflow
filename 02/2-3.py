import threading,time

def doWaiting():
    print('start waiting:',time.strftime('%S'))
    time.sleep(5)
    print('stop waiting:',time.strftime('%S'))

thread1 = threading.Thread(target = doWaiting)
thread1.start()
time.sleep(2)
print('start join')
thread1.join()
print('stop join')

thread2 = threading.Thread(target = doWaiting)

thread2.start()
time.sleep(6)
print('start join')
thread2.join
print('stop join')


