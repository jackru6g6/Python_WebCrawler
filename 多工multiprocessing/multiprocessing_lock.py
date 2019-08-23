'''
    multiprocessing共享內存.Value()
'''

import multiprocessing as mp
import time

def job(v, num, l):
    l.acquire()#Lock
    for _ in range(10):
        time.sleep(0.1)
        v.value += num
        print(v.value)
    l.release()

def multicore():
    l = mp.Lock()#避免多進程重複
    v = mp.Value('i', 0)#共享內存'i'表示整數，數字為0，最多可為一為陣列[0,1,2]
    p1 = mp.Process(target=job, args=(v, 1, l))
    p2 = mp.Process(target=job, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    multicore()