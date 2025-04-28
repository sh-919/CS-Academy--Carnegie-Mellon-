from cmu_cpcs_utils import testFunction

def getGrade(score):
    
    if not isinstance(score, (int, float)):
        return None
    
    if (score >= 90):
        return ('A')
    elif (80 <= score < 90):
        return ('B')
    elif (70 <= score < 80):
        return ('C')
    elif (60 <= score < 70):
        return ('D')
    elif (score < 60):
        return ('F')
    else:
        return None
 

@testFunction
def testGetGrade():
    assert(getGrade(99)  == 'A')
    assert(getGrade(88)  == 'B')
    assert(getGrade(77)  == 'C')
    assert(getGrade(66)  == 'D')
    assert(getGrade(55)  == 'F')


    assert(getGrade(90) == 'A')
    assert(getGrade(80) == 'B')
    assert(getGrade(70) == 'C')
    assert(getGrade(60) == 'D')

    assert(getGrade(104) == 'A')
    assert(getGrade(0) == 'F')
    assert(getGrade(-12) == 'F')
    assert(getGrade(84.2) == 'B')
    assert(getGrade(-12.2) == 'F')
    assert(getGrade(-91.3) == 'F')

    assert(getGrade(None) == None)
    assert(getGrade('ABCDE') == None)
    assert(getGrade('79') == None)

def main():
    testGetGrade()

main()
