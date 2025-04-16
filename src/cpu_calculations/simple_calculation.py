"""Simple calculation to determine CPU task time"""
import random

def simple_calc():
    random_numbers = [random.random() for i in range(100000)]
    return sum(random_numbers)


if __name__=='__main__':
    simple_calc()