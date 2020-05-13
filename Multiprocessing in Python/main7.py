import multiprocessing
import time

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.1)
        ### CS start : acquire lock
        lock.acquire()
        balance.value = balance.value + 1
        ### CS end: release lock
        lock.release()
def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.1)
        ### CS start : acquire lock
        lock.acquire()
        balance.value = balance.value - 1
        ### CS end: release lock
        lock.release()

if __name__=="__main__":
    # init balance
    balance = multiprocessing.Value('i', 200)

    ## init a lock
    lock = multiprocessing.Lock()

    d = multiprocessing.Process(target=deposit, args=(balance, lock))
    w = multiprocessing.Process(target=withdraw, args=(balance, lock))

    d.start()
    w.start()

    d.join()
    w.join()

    print (f'Final balance: {balance.value}')
