from cmu_cpcs_utils import testFunction

def babylonianSquareRootIterations(n, initialGuess, epsilon):
    guess = initialGuess
    Iterations = 0
    while True:
        new = (guess + n / guess)/2 
        Iterations += 1
        if abs(new - guess) < epsilon:
            break
        guess = new
    return Iterations

@testFunction
def testBabylonianSquareRootIterations():
    assert(babylonianSquareRootIterations(1, 1, 0.25) == 1)
    assert(babylonianSquareRootIterations(9, 3, 0.1) == 1)
    assert(babylonianSquareRootIterations(9, 3.5, 0.05) == 2)
    assert(babylonianSquareRootIterations(9, 5, 0.1) == 3)
    assert(babylonianSquareRootIterations(4, 7, 0.25) == 4)
    assert(babylonianSquareRootIterations(0.49, 2, 0.05) == 4)
    assert(babylonianSquareRootIterations(25, 10, .05) == 4)

def main():
    testBabylonianSquareRootIterations()

main()
