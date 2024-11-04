import time
import multiprocessing
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name) as file:
        for line in file:
            all_data.append(line)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = time.time()
    for name in filenames:
        read_info(name)
    finish_time = time.time()
    print(round(finish_time - start_time, 6), '(линейный)')

    start_time = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    print(datetime.now() - start_time, '(многопроцессный)')

