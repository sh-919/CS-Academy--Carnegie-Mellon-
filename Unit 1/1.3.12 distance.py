from cmu_cpcs_utils import almostEqual, testFunction
import math

def distance(x1, y1, x2, y2):
    distxvalue = (float(x2) - float(x1))**2
    distyvalue = (float(y2) - float(y1))**2
    distval = math.sqrt(distxvalue + distyvalue)
    return float(distval)
    

@testFunction
def testDistance():
    assert(almostEqual(distance(0, 0, 0, 1), 1))
    assert(almostEqual(distance(0, 0, 1, 0), 1))
    assert(almostEqual(distance(2, 0, 0, 0), 2))
    assert(almostEqual(distance(0, 2, 0, 0), 2))
    assert(almostEqual(distance(1, 5, 1, 12), 7))
    assert(almostEqual(distance(-7, -11, 5, -2), 15))
    assert(almostEqual(distance(-13, 21, 3, 51), 34))
    assert(almostEqual(distance(0, 0, 0, 0), 0))
    assert(almostEqual(distance(-2, -2, -2, -2), 0))
    assert(almostEqual(distance(5, 5, 0, 0), 5 * math.sqrt(2)))
    assert(almostEqual(distance(0, 0, -2, 4), 2 * math.sqrt(5)))
    assert(almostEqual(distance(-3, 1, -2, 4), math.sqrt(10)))
    assert(almostEqual(distance(6, 4, -5, -2), math.sqrt(157)))
    assert(type(distance(0, 0, 0, 1)) == float)

def main():
    testDistance()

main()
