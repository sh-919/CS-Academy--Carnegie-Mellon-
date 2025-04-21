from cmu_cpcs_utils import testFunction
import math

def leftoverPizzaSlices(students, slicesPerStudent):
    fullpizzas = math.ceil((students * slicesPerStudent)/8)
    totalSlice = (fullpizzas*8)
    leftover = totalSlice - (students * slicesPerStudent)
    return leftover
    
    
@testFunction
def testLeftoverPizzaSlices():
    assert(leftoverPizzaSlices(8, 1) == 0)
    assert(leftoverPizzaSlices(9, 1) == 7)
    assert(leftoverPizzaSlices(5, 4) == 4)
    assert(leftoverPizzaSlices(10, 2) == 4)
    assert(leftoverPizzaSlices(0, 0) == 0)
    assert(leftoverPizzaSlices(0, 3) == 0)
    assert(leftoverPizzaSlices(10, 0) == 0)
    assert(leftoverPizzaSlices(3, 4) == 4)

def main():
    testLeftoverPizzaSlices()

main()
