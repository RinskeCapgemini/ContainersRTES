"""Performs a heavy CPU-bound calculation by finding all primes up to n."""

def cpu_long(n=20000000):
    # Return a list of all prime numbers up to n

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
    cpu_long()