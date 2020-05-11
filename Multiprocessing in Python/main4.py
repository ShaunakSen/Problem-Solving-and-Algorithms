import time
import threading
import os

def calc_squares(numbers):
    print ('calculating sqs...')
    print (f'process id: {os.getpid()}')
    for n in numbers:
        time.sleep(0.2)
        print (f'sq of {n} is {n**2}')

def calc_cubes(numbers):
    print ('calculating cubes...')
    print (f'process id: {os.getpid()}')
    for n in numbers:
        time.sleep(0.2)
        print (f'cube of {n} is {n**3}')


print (f'Main process id: {os.getpid()}')
arr = [2,3,8,9]

t = time.time()

## create 2 threads

t1 = threading.Thread(target=calc_squares, args=(arr, ))
t2 = threading.Thread(target=calc_cubes, args=(arr, ))

## start the threads: executes the 2 functions in parallel
t1.start()
t2.start()

## join: wait until that particular thread is done]
t1.join()
t2.join()


print(f'Completed in {time.time() - t} seconds')