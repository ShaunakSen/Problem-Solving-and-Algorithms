import numpy as np
from multiprocessing import Pool
import time
from functools import partial

def process_curr_week():
    time.sleep(1)
    return

def process_request(week, req):
    print (f'Processing req: {req} for week: {week}')
    time.sleep(1)
    return [week, req]


def main():

    all_results = []
    currentweeks = list(range(1, 5))
    requests = {'1': [10,11,12,13], '2': [14,15,16], '3': [17], '4': [18,19,20]}

    for week in currentweeks:
        ## get the requests for this week

        requests_for_this_week = requests[str(week)]
        p = Pool()
        func = partial(process_request, week)
        results = p.map(func, requests_for_this_week)
        p.close()
        p.join()
        all_results.append(results)
        # for req in requests_for_this_week:
        #     all_results.append(process_request(week, req))
    print (all_results)

"""
1. Parallelize requests
"""

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print (f'Total execution time: {end_time-start_time}')