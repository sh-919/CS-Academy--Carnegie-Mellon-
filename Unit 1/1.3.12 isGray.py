from cmu_cpcs_utils import testFunction

def isGray(rgb):
    grnblu = rgb % 1000000
    grn = grnblu // 1000
    blu = grnblu % 1000
    red = rgb // 1000000
    return grn == blu == red



@testFunction
def testIsGray():
    assert(isGray(112112112) == True)
    assert(isGray(112112113) == False)
    assert(isGray(123195060) == False)
    assert(isGray(255255255) == True)
    assert(isGray(0) == True)
    assert(isGray(19019019) == True)
    assert(isGray(175112) == False)

def main():
    testIsGray()

main()
