"""Intense calculation for CPU time"""
import time 

def log_result(duration):
    with open("log_files/long_calc_log.txt", "a") as log_file:
        log_file.write(f"Task time = {duration}\n")

    print(f"Task time = {duration}\n")

def long_calculation(n):
    primes = [True] * (n + 1)

    primes[0] = False
    primes[1] = False

    for number in range(2, n + 1):
        if primes[number]:
            for multiple in range(number * 2, n + 1, number):
                primes[multiple] = False

    result = []
    for i in range(n + 1):
        if primes[i]:
            result.append(i)

    return result

if __name__=='__main__':

    start_time = time.time()

    long_calculation(20000000)

    duration = time.time() - start_time

    log_result(duration)