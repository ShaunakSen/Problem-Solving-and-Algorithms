## Multiprocessing in Python Guide

> Based on the tutorial by DataFlair: https://data-flair.training/blogs/python-multiprocessing/

---

### Python Multiprocessing Process Class

Let’s talk about the Process class in Python Multiprocessing first. This is an abstraction to set up another process and lets the parent application control execution. Here, we observe the start() and join() methods. Let’s first take an example.

NOTE: accessing global vars is not so straightforward inside the individual processes

This is because each process starts of simultanously. So at the start each has the value `[None, None, None, None]` as value of `global_var_list`, so the first process modifies it as `[True, None, None, None]`, the second as `[None, True, None, None]` and not `[True, True, None, None]`

Code:

``` python

import multiprocessing
from multiprocessing import Process
import random

global_var_list = [None]*4



def heavy_op1(i,n):
    """
    simple resource intensive function
    """
    global global_var_list
    print (f'Started with n: {n}')
    print (f'Setting global var at idx: {i-1}')
    global_var_list[i-1] = True
    x = sorted([random.random() for i in range(n)])
    print ('Function idx: ', i, len(x))
    print ('Function idx: ',i, global_var_list)


def main():
    p1 = Process(target=heavy_op1, args=(1, 10000000,))
    p2 = Process(target=heavy_op1, args=(2, 70000000,))
    p3 = Process(target=heavy_op1, args=(3, 40000000,))
    p4 = Process(target=heavy_op1, args=(4, 20000000,))
    ### start the processes
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    ### stop execution
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    print("We're done")
    print ('Global var at end of processing:', global_var_list)
if __name__=="__main__":
    main()
```

Output:

```
Started with n: 70000000
Setting global var at idx: 1
Started with n: 10000000
Setting global var at idx: 0
Started with n: 20000000
Setting global var at idx: 3
Started with n: 40000000
Setting global var at idx: 2
Function idx:  1 10000000
Function idx:  1 [True, None, None, None]
Function idx:  4 20000000
Function idx:  4 [None, None, None, True]
Function idx:  3 40000000
Function idx:  3 [None, None, True, None]
Function idx:  2 70000000
Function idx:  2 [None, True, None, None]
We're done
Global var at end of processing: [None, None, None, None]
```