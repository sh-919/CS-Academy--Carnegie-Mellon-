from cmu_cpcs_utils import testFunction

def dotsOverlap(x1, y1, r1, x2, y2, r2):
    a = (x1 - x2)**2 + (y1 - y2)**2 <= (r1+r2)**2
    return a

@testFunction
def testDotsOverlap():
    assert(dotsOverlap(0, 0, 2, 3, 0, 2) == True)
    assert(dotsOverlap(0, 0, 2, 5, 0, 2) == False)
    assert(dotsOverlap(0, 0, 2, 4, 0, 2) == True)
    assert(dotsOverlap(-4, 5, 2, -3, 5, 5) == True)
    assert(dotsOverlap(3, 3, 3, 3, -3, 2.99) == False)
    assert(dotsOverlap(3, 3, 3, 3, -3, 3) == True)
    assert(dotsOverlap(5, 3, 0, 5, 3, 0) == True)

def main():
    testDotsOverlap()

main()
