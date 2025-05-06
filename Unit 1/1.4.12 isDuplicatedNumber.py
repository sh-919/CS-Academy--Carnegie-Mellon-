from cmu_cpcs_utils import testFunction
import math

def isDuplicatedNumber(n):
    if n == 0:
        return False
    if n < 0:
        n = abs(n)
        
    if n < 10:
        return False
        
    n_digits = int(math.log10(n)) + 1
    
    if n_digits % 2 != 0:
        return False
    
    half_l = n_digits // 2
    divisor = 10 ** half_l
    right = n % divisor
    left = n // divisor
    
    return  left == right

@testFunction
def testIsDuplicatedNumber():
    assert(isDuplicatedNumber(11) == True)
    assert(isDuplicatedNumber(55) == True)
    assert(isDuplicatedNumber(123123) == True)
    assert(isDuplicatedNumber(123) == False)
    assert(isDuplicatedNumber(1221) == False)
    assert(isDuplicatedNumber(12312) == False)
    assert(isDuplicatedNumber(121212) == False)
    assert(isDuplicatedNumber(1) == False)
    assert(isDuplicatedNumber(0) == False)
    
def main():
    testIsDuplicatedNumber()

main()
