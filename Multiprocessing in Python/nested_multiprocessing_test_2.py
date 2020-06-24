import numpy as np
from multiprocessing import Pool
import time
from functools import partial

def process_curr_week(requests, week):
    all_requests = get_requests_for_week(week, requests)
    p = Pool()
    func = partial(process_request, week)
    results = p.map(func, all_requests)
    return results

def process_request(week, req):
    print (f'Processing req: {req} for week: {week}')
    time.sleep(1)
    return [week, req]

def get_requests_for_week(week, requests):
    return requests[str(week)]

def process_curr_week_seq(requests, week):
    all_requests = get_requests_for_week(week, requests)
    results_this_week = []
    for req in all_requests:
        results_this_week.append(process_request(week, req))
    return results_this_week

def main():

    all_results = []
    currentweeks = list(range(1, 5))
    requests = {'1': [10,11,12,13], '2': [14,15,16], '3': [17], '4': [18,19,20]}

    p1 = Pool()
    func1 = partial(process_curr_week_seq, requests)
    all_results = p1.map(func1, currentweeks)
    print (all_results)
    p1.close()
    p1.join()


    # for week in currentweeks:
    #     ## get the requests for this week

    #     requests_for_this_week = requests[str(week)]
    #     p = Pool()
    #     func = partial(process_request, week)
    #     results = p.map(func, requests_for_this_week)
    #     all_results.append(results)
    #     # for req in requests_for_this_week:
    #     #     all_results.append(process_request(week, req))
    # print (all_results)

"""
1. Parallelize requests (11-6.2)
2. Parallelize curweek (11-5.61)
3. 
"""

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print (f'Total execution time: {end_time-start_time}')