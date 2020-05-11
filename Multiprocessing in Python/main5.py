import multiprocessing


def calc_squares(numbers, result, value):
    value.value = 5.0
    for idx, n in enumerate(numbers):
        result[idx] = n**2
    print (f'Within process: {result[:]}, {value.value}')

if __name__=="__main__":
    numbers = [2,3,5]
    # create a shared memory var
    result = multiprocessing.Array('i', 3)
    value = multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target=calc_squares, args=(numbers, result, value))

    p.start()
    p.join()

    print(f'Outside process {result[:]},{value.value}')