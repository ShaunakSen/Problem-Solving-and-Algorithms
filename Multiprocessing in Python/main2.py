import multiprocessing
from multiprocessing import Process, current_process
import random
import os

test_list = [1,2,3] 


def heavy_op1(i,n):
    """
    simple resource intensive function
    """
    global test_list
    print (f'Function idx: {i}, global: {test_list}')
    print (f'Started with n: {n}')
    x = sorted([random.random() for i in range(n)])
    print (f'Function idx: {i}, length: {len(x)}, function name: {current_process().name}')
    print (f'Function pid: {os.getpid()}')


def main():
    global test_list
    test_list = [3,4,5]
    print (f'Parent id: {os.getpid()}')
    p1 = Process(target=heavy_op1, args=(1, 40000000,), name='process 1')
    p2 = Process(target=heavy_op1, args=(2, 60000000,))
    ### start the processes
    p1.start()
    p2.start()
    
    ### stop execution
    p1.join()
     ### p2 alive False p1 alive False
    print (f'p1 alive:? {p1.is_alive()}') 
    p2.join()
    print (f'p2 alive:? {p2.is_alive()}')
    
    print("We're done")
if __name__=="__main__":
    main()