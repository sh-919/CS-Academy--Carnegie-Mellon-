from cmu_cpcs_utils import almostEqual, testFunction

def getInRange(x, bound1, bound2):
    low = min(bound1, bound2)
    upp = max(bound1, bound2)
    if x < low:
        return low
    elif x > upp:
        return upp
    else:
        return x

@testFunction
def testGetInRange():
    assert(getInRange(1, 3, 5) == 3)
    assert(getInRange(4, 3, 5) == 4)
    assert(getInRange(6, 5, 3) == 5)
    assert(getInRange(5, 5, 3) == 5)
    assert(getInRange(-1, -3, -5) == -3)
    assert(getInRange(-4, -5, -3) == -4)
    assert(getInRange(-6, -6, -3) == -6)
    assert(almostEqual(getInRange(6.2, 6.3, 6.4), 6.3))

def main():
    testGetInRange()

main()
