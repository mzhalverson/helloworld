O = "to infinity and beyond"
def addAlg(p1,p2,a):
    if p1 == O:
        p3 = p2
    elif p2 == O:
        p3 = p1
    elif p1[0] == p2[0] and p1[1] == -p2[1]:
        p3 = O 
    elif p1 == p2:
        m = slopeCalc_same(p1,a)
        x3 = m**2 - p1[0]-p2[0]
        y3 = m*(p1[0]-x3) - p1[1]
        p3 = (x3,y3) 
    else:
        m = slopeCalc_diff(p1,p2)
        x3 = m**2 - p1[0]-p2[0]
        y3 = m*(p1[0]-x3) - p1[1]
        p3 = (x3,y3) 
    return p3


def slopeCalc_same(p1,a):
    return (3*(p1[0]**2)+a)/(2*p1[1])


def slopeCalc_diff(p1,p2):
    return (p2[1]-p1[1])/(p2[0]-p1[0])


print(addAlg((7,16),(1,2),-15))
