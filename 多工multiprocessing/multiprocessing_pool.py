import multiprocessing as mp

'''
multiprocessing的pool可以讓程式規劃多工的順序及使用
'''

def job(x):
    return x*x

def multicore():
    pool = mp.Pool(processes=2)#mp.Pool()若()，則預設是電腦全部核心數，processes=2則是指定兩核
    res = pool.map(job, range(10))#map可以一次多個，自動分配給多少進程
    print(res)
    
    res = pool.apply_async(job, (2,))#apply_async只會執行一核，(2,)的,表示參數可以被疊代，不可多核(2,3,4)會錯誤
    print(res.get())

    multi_res =[pool.apply_async(job, (i,)) for i in range(10)]#apply_async參數疊代，此方法跟pool的map方法一樣
    print([res.get() for res in multi_res])#列表疊代，一一取值

if __name__ == '__main__':
    multicore()