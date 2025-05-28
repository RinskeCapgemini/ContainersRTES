"""Medium intensity calculation for CPU time"""

def fibonacci(n):
    # Recursive fibonacci function.

    if n <= 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)

def cpu_medium(n=30):
    # Calculate Fibonacci numbers up to n using recursion.

    for i in range(n):
        fibonacci(i)


if __name__=='__main__':
    cpu_medium()
