"""Simple calculation to determine CPU task time"""
import random
import time

def log_result(duration):
    with open("log_files/simple_calc_log.txt", "a") as log_file:
        log_file.write(f"Task time = {duration}\n")

    print(f"Task time = {duration}\n")

def basic_calculation():
    random_numbers = [random.random() for i in range(100000)]

    return sum(random_numbers)

if __name__=='__main__':

    start_time = time.time()

    basic_calculation()

    duration = time.time() - start_time
    
    log_result(duration)
