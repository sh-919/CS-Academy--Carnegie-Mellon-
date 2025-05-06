from cmu_cpcs_utils import testFunction

def chicagoHour(parisHour):
    gohour24 = (parisHour - 7) % 24
    gohour12 = gohour24 % 12
    if gohour12 == 0:
        return 12
    else:
        return gohour12

@testFunction
def testChicagoHour():
    assert(chicagoHour(0) == 5)
    assert(chicagoHour(3) == 8)
    assert(chicagoHour(7) == 12)
    assert(chicagoHour(8) == 1)
    assert(chicagoHour(12) == 5)
    assert(chicagoHour(15) == 8)
    assert(chicagoHour(19) == 12)
    assert(chicagoHour(20) == 1)
    assert(chicagoHour(23) == 4)

def main():
    testChicagoHour()

main()
