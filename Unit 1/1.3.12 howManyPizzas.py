from cmu_cpcs_utils import testFunction
import math

def howManyPizzas(students, slicesPerStudent):
    totalSlicewrk = students * slicesPerStudent
    totalSlice = math.ceil(totalSlicewrk/8)
    return totalSlice 

@testFunction
def testHowManyPizzas():
    assert(howManyPizzas(8, 1) == 1)
    assert(howManyPizzas(9, 1) == 2)
    assert(howManyPizzas(5, 4) == 3)
    assert(howManyPizzas(10, 2) == 3)
    assert(howManyPizzas(0, 0) == 0)
    assert(howManyPizzas(0, 3) == 0)
    assert(howManyPizzas(10, 0) == 0)
    assert(howManyPizzas(3, 4) == 2)

def main():
    testHowManyPizzas()

main()
