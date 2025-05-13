from cmu_cpcs_utils import testFunction, rounded


def isPrime(n):
    if n < 2: 
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    maxfactor = rounded(n ** 0.5)
    for factor in range(3, maxfactor + 1, 2):
        if n % factor == 0:
            return False
    return True

def nthPrime(n):
    pF = 0
    pTF = n + 1
    g = 0
    lastPF = None
    while pF < pTF:
        g += 1
        if isPrime(g):
            pF += 1 
            lastPF = g
    return lastPF

@testFunction
def testNthPrime():
    assert(nthPrime(0) == 2)
    assert(nthPrime(1) == 3)
    assert(nthPrime(2) == 5)
    assert(nthPrime(3) == 7)
    assert(nthPrime(4) == 11)
    assert(nthPrime(5) == 13)

def main():
    testNthPrime()

main()
