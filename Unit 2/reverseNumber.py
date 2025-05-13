from cmu_cpcs_utils import testFunction

def reverseNumber(n):
    sign = 1 if n >= 0 else -1
    n = abs(n)
    result = 0
    while n > 0:
        cDig = n % 10
        result *= 10
        result += cDig
        n //= 10
    return result * sign

@testFunction
def testReverseNumber():
    assert(reverseNumber(12345) == 54321)
    assert(reverseNumber(34) == 43)
    assert(reverseNumber(0) == 0)
    assert(reverseNumber(1) == 1)
    assert(reverseNumber(10) == 1)
    assert(reverseNumber(2500) == 52)
    assert(reverseNumber(-12345) == -54321)
    assert(reverseNumber(-1) == -1)

def main():
    testReverseNumber()

main()
