from cmu_cpcs_utils import almostEqual, testFunction
import math

def triangleArea(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    s = (a + b + c) / 2
    a1 = s*(s-a)*(s-b)*(s-c)
    area = math.sqrt(a1)
    return float(area)

@testFunction
def testTriangleArea():
    assert(almostEqual(triangleArea(3, 4, 5), 6))
    assert(almostEqual(triangleArea(15, 9, 12), 54))
    assert(almostEqual(triangleArea(7, 25, 24), 84))
    assert(almostEqual(triangleArea(8, 15, 17), 60))
    assert(almostEqual(triangleArea(0, 0, 0), 0))
    assert(almostEqual(triangleArea(1, 1, 1), math.sqrt(3)/4))
    assert(almostEqual(triangleArea(5, 5, 5), 25*math.sqrt(3)/4))
    assert(almostEqual(triangleArea(12, 12, 12), 144*math.sqrt(3)/4))
    assert(almostEqual(triangleArea(7, 12, 18), math.sqrt(11063)/4))
    assert(almostEqual(triangleArea(9.1, 11.7, 3), 7*math.sqrt(3026)/50))

def main():
    testTriangleArea()

main()
