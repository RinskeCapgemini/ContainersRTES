"""Intense calculation for CPU time"""
import time 

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

    long_calculation(2000000)

    duration = time.time() - start_time

    print(f"Task time = {duration}")

