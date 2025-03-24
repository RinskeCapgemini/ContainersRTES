"""Medium intensity calculation for CPU time"""

def fibonacci(n):
    if n <= 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)

def mid_calc(n=40):
    for i in range(n):
        fibonacci(i)


