"""Heavy calculation for CPU time"""

def long_calc(n=20000000):
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
    long_calc()