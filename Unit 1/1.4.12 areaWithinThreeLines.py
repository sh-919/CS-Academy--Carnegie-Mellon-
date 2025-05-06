from cmu_cpcs_utils import almostEqual, testFunction
import math


def intersection(m1, b1, m2, b2):
    if m1 == m2:
        return None
    return (b2 - b1) / (m1 - m2)

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2 - y1)**2)

def area(a, b, c):
    s = (a + b + c) / 2
    if s <= a or s <= b or s <= c:
        return 0
    return math.sqrt(s * (s-a) * (s - b) * (s - c))

def areaWithinThreeLines(m1, b1, m2, b2, m3, b3):
    xa = intersection(m1, b1, m2, b2)
    xb = intersection(m1, b1, m3, b3)
    xc = intersection(m2, b2, m3, b3)
    
    if xa is None or xb is None or xc is None:
        return None
    
    ya = m1 * xa + b1
    yb = m1 * xb + b1
    yc = m2 * xc + b2
    
    s1 = distance(xa, ya, xb, yb)
    s2 = distance(xa, ya, xc, yc)
    s3 = distance(xb, yb, xc, yc)
    
    total_area = area(s1, s2, s3)
    
    if area == 0:
        return None
    else:
        return total_area

@testFunction
def testAreaWithinThreeLines():
    assert(almostEqual(areaWithinThreeLines(0, 7, 1, 0, -1, 2), 36))
    assert(almostEqual(areaWithinThreeLines(1, -5, 0, -2, 2, 2), 25))
    assert(almostEqual(areaWithinThreeLines(0, -9.75, -6, 2.25, 1, -4.75), 21))
    assert(almostEqual(areaWithinThreeLines(1, -5, 0, -2, 2, 25), 272.25))
    assert(almostEqual(areaWithinThreeLines(1, 2, 3, 4, 5, 6), 0))

    # The first two lines are parallel:
    assert(areaWithinThreeLines(1, 2, 1, 4, 0, 7) == None)

    # Here, the second and third lines are parallel
    assert(areaWithinThreeLines(5, 2, 1, 4, 1, 6) == None)

def main():
    testAreaWithinThreeLines()

main()
