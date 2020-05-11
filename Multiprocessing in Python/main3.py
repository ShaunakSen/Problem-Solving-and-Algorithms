import multiprocessing
from multiprocessing import Process, current_process, Lock
import random
import os


lock = Lock()

global_list = [None]*3

def heavy_op1(i,n):
    """
    simple resource intensive function
    """
    lock.acquire()
    global global_list
    print (f'Started with n: {n}')
    x = sorted([random.random() for i in range(n)])
    print (f'Setting global position of idx: {i}')
    global_list[i] = True
    print (f'idx: {i} global list: {global_list}')
    print (f'Function idx: {i}, length: {len(x)}, function name: {current_process().name}')
    print (f'Function pid: {os.getpid()}')
    lock.release()


def main():
    print (f'Parent id: {os.getpid()}')

    numbers_to_run = [40000000, 10000000, 60000000]

    for idx in range(len(numbers_to_run)):
        p = Process(target=heavy_op1, args=(idx, numbers_to_run[idx]))
        p.start()
    
    print("We're done")
if __name__=="__main__":
    main()