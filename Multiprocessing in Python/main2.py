import multiprocessing
from multiprocessing import Process
import random
import os


def heavy_op1(i,n):
    """
    simple resource intensive function
    """
    print (f'Started with n: {n}')
    x = sorted([random.random() for i in range(n)])
    print ('Function idx: ', i, len(x))
    print (f'Function pid: {os.getpid()}')


def main():
    print (f'Parent id: {os.getpid()}')
    p1 = Process(target=heavy_op1, args=(1, 40000000,))
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