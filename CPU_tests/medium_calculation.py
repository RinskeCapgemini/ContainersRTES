"""Medium intensity calculation for CPU time"""
import time

def log_result(duration):
    with open("log_files/mid_calc_log.txt", "a") as log_file:
        log_file.write(f"Task time = {duration}\n")

    print(f"Task time = {duration}\n")

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

    log_result(duration)
