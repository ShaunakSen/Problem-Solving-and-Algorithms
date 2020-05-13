from multiprocessing import Pool
import time

def f(n):
    sum=0
    for x in range(10000):
        sum+=x**2
    return sum

if __name__ == "__main__":
    t1 = time.time()
    p = Pool()
    # map is used to divide the work into multiple cores
    # this will automatically div the work among all cpu cores
    # and it will return the result
    result = p.map(func=f, iterable=range(10000))
    p.close()
    p.join()

    print (f'Pool took {time.time() - t1}s')
    print (f'Result sum: {sum(result)}')

    t2 = time.time()
    result = []
    for x in range(10000):
        result.append(f(x))

    print(f'Serial operaltion took {time.time() - t2}s')
    print (f'Result sum: {sum(result)}')