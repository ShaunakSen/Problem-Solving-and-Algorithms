import multiprocessing

def cal_squares(idx, numbers, q):
    for n in numbers:
        q.put({'id': idx, 'value': n**2})


if __name__=="__main__":
    numbers = [3,4,5]
    numbers2 = [9,8,7]

    q1, q2 = multiprocessing.Queue(), multiprocessing.Queue()
    p1 = multiprocessing.Process(target=cal_squares, args=(1, numbers, q1))
    p2 = multiprocessing.Process(target=cal_squares, args=(2, numbers2, q2))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    while not q1.empty():
        print(q1.get())

    while not q2.empty():
        print(q2.get())