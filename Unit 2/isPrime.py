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
        
@testFunction
def testIsPrime():
    assert(isPrime(1) == False)
    assert(isPrime(2) == True)
    assert(isPrime(7) == True)
    assert(isPrime(8) == False)
    assert(isPrime(9) == False)
    assert(isPrime(0) == False)
    assert(isPrime(-1) == False)
    assert(isPrime(-7) == False)

def main():
    testIsPrime()

main()
