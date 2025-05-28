"""Simple calculation to determine CPU task time"""
import random

def cpu_low():
    # Perform a simple calculation by summing 100,000 random numbers.

    random_numbers = [random.random() for i in range(100000)]
    return sum(random_numbers)


if __name__=='__main__':
    cpu_low()