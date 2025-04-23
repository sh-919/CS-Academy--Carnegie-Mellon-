from cmu_cpcs_utils import testFunction

def getGreen(rgb):
    grnblu = rgb % 1000000
    grn = grnblu // 1000
    return grn

@testFunction
def testGetGreen():
    assert(getGreen(218112214) == 112)
    assert(getGreen(134134134) == 134)
    assert(getGreen(111019213) == 19)
    assert(getGreen(221000000) == 0)
    assert(getGreen(32175) == 32)
    assert(getGreen(0) == 0)

def main():
    testGetGreen()

main()
