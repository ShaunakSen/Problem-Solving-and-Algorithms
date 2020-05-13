import multiprocessing
import time
def calc_squares(i, numbers, q):
    for idx, n in enumerate(numbers):
        # push to queue
        q.put({'idx': idx, 'n_sq': str(n**2)})

if __name__=="__main__":
    numbers1, numbers2 = [2,3,5], [5,6,7]
    
    # create two queues
    q1 = multiprocessing.Queue()
    q2 = multiprocessing.Queue()

    # create 2 processes
    p1 = multiprocessing.Process(target=calc_squares, args=(1, numbers1, q1))
    p2 = multiprocessing.Process(target=calc_squares, args=(2, numbers2, q2))


    p1.start()
    p2.start()

    p1.join()
    p2.join()



    while not q1.empty():
        print (f'Within main: {q1.get()}')
    while not q2.empty():
        print (f'Within main: {q2.get()}')

    print (f'Is q1 empty: {q1.empty()}')
    print (f'Is q2 empty: {q2.empty()}')

    print ('End of main...')