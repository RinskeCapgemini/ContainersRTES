"""Medium intensity calculation for CPU time"""
import time


def fibonacci(n):
    if n <= 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)

def medium_calculation(n):
    for i in range(n):
        fibonacci(i)


if __name__=='__main__':

    start_time = time.time()

    medium_calculation(30)

    duration = time.time() - start_time

    print(f"Task time = {duration}")

