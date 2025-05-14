from cmu_cpcs_utils import testFunction

def gcd(x, y):
    while (y):
        x, y = y, x % y 
    return x

@testFunction
def testGcd():
    assert(gcd(3, 3) == 3)
    assert(gcd(3**6, 3**6) == 3**6)
    assert(gcd(3**6, 2**6) == 1)
    assert(gcd(2*3*4*5, 3*5) == 15)
    x = 1568160 # 2**5 * 3**4 * 5**1 * 11**2
    y = 3143448 # 2**3 * 3**6 * 7**2 * 11**1
    g = 7128    # 2**3 * 3**4 *        11**1
    assert(gcd(x, y) == g)

def main():
    testGcd()

main()
