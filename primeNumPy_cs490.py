import sys

primeCount = int (sys.argv[1])

def isPrime(a: int) -> bool:
    if (a == 1):
        return False
    if (a == 2):
        return True
    sqrt_a = a ** 0.5
    i = 2
    while (i <= sqrt_a):
        if (a % i == 0):
            return False
        i += 1
    return True

counter = 1

while primeCount != 0:
    if isPrime(counter):
        print (counter)
        primeCount -= 1
    counter += 1
    



