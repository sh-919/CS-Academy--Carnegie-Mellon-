from cmu_cpcs_utils import testFunction

def numberOfBricks(steps):
    return steps*(steps+1)/2

@testFunction
def testNumberOfBricks():
    assert(numberOfBricks(0) == 0)
    assert(numberOfBricks(1) == 1)
    assert(numberOfBricks(2) == 3)
    assert(numberOfBricks(3) == 6)
    assert(numberOfBricks(4) == 10)
    assert(numberOfBricks(10) == 55)

def main():
    testNumberOfBricks()

main()
