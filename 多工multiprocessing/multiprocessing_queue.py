'''
多工(多核運算)
'''

import multiprocessing as mp

def job(q):#multiprocessing的target function不可以有return，所以必須將須回傳的data放入queue
    res = 0
    for i in range(1000):
        res += i+i**2+i**3
    q.put(res) # queue

if __name__ == '__main__':
    q = mp.Queue()#定義multiprocessing的queue
    p1 = mp.Process(target=job, args=(q,))#若需要queue，必須queue傳入function(reference)，若只有一項參數(args)，必須要,
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()#multiprocessing的join表示要等多工執行完成，再繼續執行當前進程
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1+res2)