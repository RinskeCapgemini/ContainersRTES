"""Simple calculation to determine CPU task time"""

import random
import os
import time


def basic_calculation():
    random_numbers = [random.random() for i in range(100000)]

    return sum(random_numbers)



if __name__=='__main__':
    print(f"Operating on CPU core: {os.sched_getcpu()}")

    start_time = time.time()

    basic_calculation()

    duration = time.time() - start_time

    print(f"Task time = {duration}")

