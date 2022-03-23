#################################################
# extra_practice1.py (due never)
#
# Your name:
# Your andrew id:
#################################################

import cs112_s22_week1_linter
import math

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

def fabricYards(inches):
    '''
    Fabric must be purchased in whole yards, so purchasing just 1 inch of fabric requires purchasing 1 entire yard. With this in mind, write the function fabricYards(inches) that takes the number of inches of fabric desired, and returns the smallest number of whole yards of fabric that must be purchased.
    '''
    if inches%36 == 0:
        yards = (inches//36)
    else:
        yards = (inches//36) + 1
    return yards

 
def fabricExcess(inches):
    '''
    Write the function fabricExcess(inches) that takes the number of inches of fabric desired and returns the number of inches of excess fabric that must be purchased (as purchases must be in whole yards). Hint: you may want to use fabricYards, which you just wrote!
    '''
    purchased = fabricYards(inches) * 36
    excess = purchased - inches
    return excess

def isEvenPositiveInt(x):
    '''
    Write the function isEvenPositiveInt(x) that takes an arbitrary value x, return True if it is an integer, and it is positive, and it is even (all 3 must be True), or False otherwise. Do not crash if the value is not an integer. So, isEvenPositiveInt("yikes!") returns False (rather than crashing), and isEvenPositiveInt(123456) returns True.
    '''
    if isinstance(x, int) and x>0 and x%2 == 0:
        return True
    else:
        return False

def nthFibonacciNumber(n):
    '''
    斐波纳契数列的黄金比例公式：https://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html
    '''
    n += 1
    golden_ratio = 5**(1/2)
    result = ((1+golden_ratio)**n-(1-golden_ratio)**n)/(2**n*golden_ratio)
    return int(result)

def isLegalTriangle(s1,s2,s3):
    max_side = max(s1, s2, s3)
    min_side = min(s1, s2, s3)
    mid_side = s1+s2+s3-max_side-min_side
    if max_side < min_side+mid_side:
        return True
    else:
        return False

def distance(x1, y1, x2, y2):
    width = abs(x1-x2)
    height = abs(y1-y2)
    distance = (width**2+height**2)**(1/2)
    return distance

def lengths(x1, y1, x2, y2, x3, y3):
    length1 = distance(x1,y1,x2,y2)
    length2 = distance(x1,y1,x3,y3)
    length3 = distance(x2,y2,x3,y3)
    return length1, length2, length3

def sort(x,y,z):
    max_num = max(x,y,z)
    min_num = min(x,y,z)
    mid_num = x+y+z-max_num-min_num
    return min_num, mid_num, max_num

def isRightTriangle(x1, y1, x2, y2, x3, y3):
    """
    right triangle
    """
    length1, length2, length3 = lengths(x1, y1, x2, y2, x3, y3)
    min_length, mid_length, max_length = sort(length1, length2, length3)
    cal_max_length = (min_length**2+mid_length**2)**.5
    if almostEqual(cal_max_length, max_length):
        return True
    else:
        return False

def triangleArea(s1, s2, s3):
    """
    海伦公式
    """
    if s1 <= 0 or s2 <= 0 or s3 <= 0:
        return 0
    else:
        semi_perimter = (s1+s2+s3)/2
        tri_area = ((semi_perimter-s1)*(semi_perimter-s2)*(semi_perimter-s3)*semi_perimter)**.5
        return tri_area


def triangleAreaByCoordinates(x1, y1, x2, y2, x3, y3):
    length1, length2, length3 = lengths(x1, y1, x2, y2, x3, y3)
    tri_area = triangleArea(length1, length2, length3)
    return tri_area

def lineIntersection(m1, b1, m2, b2):
    '''
    This function returns the x value of the point of intersection of the two lines. If the lines are parallel, or identical, the function should return None.
    '''
    if m1-m2 == 0:
        return None
    else:
        x_coordinate = (b2-b1)/(m1-m2)
        return x_coordinate

def line_intersection_points(m1, b1, m2, b2, m3, b3):
    x1 = lineIntersection(m1,b1,m2,b2)
    y1 = m1*x1+b1
    x2 = lineIntersection(m1,b1,m3,b3)
    y2 = m1*x2+b1
    x3 = lineIntersection(m3,b3,m2,b2)
    y3 = m2*x3+b2
    return x1, y1, x2, y2, x3, y3

def threeLinesArea(m1, b1, m2, b2, m3, b3):
    x1, y1, x2, y2, x3, y3 = line_intersection_points(m1, b1, m2, b2, m3, b3)
    tri_area = triangleAreaByCoordinates(x1, y1, x2, y2, x3, y3)
    return tri_area



def rectanglesOverlap(x1, y1, w1, h1, x2, y2, w2, h2):
    """A rectangle can be described by its left, top, width, and height. This function takes two rectangles described this way, and returns True if the rectangles overlap at all (even if just at a point), and False otherwise. Note: here we will represent coordinates the way they are usually represented in computer graphics, where (0,0) is at the left-top corner of the screen, and while the x-coordinate goes up while you head right, the y-coordinate goes up while you head down (so we say that "up is down").
    只要判断是否相交即可
    """
    x11 = x1+w1
    y11 = y1+h1
    x22 = x2+w2
    y22 = y2+h2
    #left case
    if x2>=x1:
        if x2<=x11:
            if y1<=y2:#down case
                if y2<=y11:
                    return True
                else:
                    return False
            else: #upper case
                if y22>=y1:
                    return True
                else:
                    return False
        else:
            return False
    else:#right case
        if x22>=x1:
            if y1<=y2:#down case
                if y2<=y11:
                    return True
                else:
                    return False
            else: #upper case
                if y22>=y1:
                    return True
                else:
                    return False



#################################################
# Test Functions
#################################################

def testFabricYards():
    print('Testing fabricYards()... ', end='')
    assert(fabricYards(0) == 0)
    assert(fabricYards(1) == 1)
    assert(fabricYards(35) == 1)
    assert(fabricYards(36) == 1)
    assert(fabricYards(37) == 2)
    assert(fabricYards(72) == 2)
    assert(fabricYards(73) == 3)
    assert(fabricYards(108) == 3)
    assert(fabricYards(109) == 4)
    print('Passed.')
 
def testFabricExcess():
    print('Testing fabricExcess()... ', end='')
    assert(fabricExcess(0) == 0)
    assert(fabricExcess(1) == 35)
    assert(fabricExcess(35) == 1)
    assert(fabricExcess(36) == 0)
    assert(fabricExcess(37) == 35)
    assert(fabricExcess(72) == 0)
    assert(fabricExcess(73) == 35)
    assert(fabricExcess(108) == 0)
    assert(fabricExcess(109) == 35)
    print('Passed.')

def testIsEvenPositiveInt():
    print('Testing isEvenPositiveInt()... ', end='')
    assert(isEvenPositiveInt(809) == False)
    assert(isEvenPositiveInt(810) == True)
    assert(isEvenPositiveInt(2389238001) == False)
    assert(isEvenPositiveInt(2389238000) == True)
    assert(isEvenPositiveInt(-2389238000) == False)
    assert(isEvenPositiveInt(0) == False)
    assert(isEvenPositiveInt('do not crash here!') == False)
    print('Passed.')

def testNthFibonacciNumber():
    print('Testing nthFibonacciNumber()... ', end='')
    assert(nthFibonacciNumber(0) == 1)
    assert(nthFibonacciNumber(1) == 1)
    assert(nthFibonacciNumber(2) == 2)
    assert(nthFibonacciNumber(3) == 3)
    assert(nthFibonacciNumber(4) == 5)
    assert(nthFibonacciNumber(5) == 8)
    assert(nthFibonacciNumber(6) == 13)
    print('Passed.')

def testIsLegalTriangle():
    print('Testing isLegalTriangle()... ', end='')
    assert(isLegalTriangle(3, 4, 5) == True)
    assert(isLegalTriangle(5, 4, 3) == True)
    assert(isLegalTriangle(3, 5, 4) == True)
    assert(isLegalTriangle(0.3, 0.4, 0.5) == True)
    assert(isLegalTriangle(3, 4, 7) == False)
    assert(isLegalTriangle(7, 4, 3) == False)
    assert(isLegalTriangle(3, 7, 4) == False)
    assert(isLegalTriangle(5, -3, 1) == False)
    assert(isLegalTriangle(-3, -4, -5) == False)
    print('Passed.')

def testIsRightTriangle():
    print('Testing isRightTriangle()... ', end='')
    assert(isRightTriangle(0, 0, 0, 3, 4, 0) == True)
    assert(isRightTriangle(1, 1.3, 1.4, 1, 1, 1) == True)
    assert(isRightTriangle(9, 9.12, 8.95, 9, 9, 9) == True)
    assert(isRightTriangle(0, 0, 0, math.pi, math.e, 0) == True)
    assert(isRightTriangle(0, 0, 1, 1, 2, 0) == True)
    assert(isRightTriangle(0, 0, 1, 2, 2, 0) == False)
    assert(isRightTriangle(1, 0, 0, 3, 4, 0) == False)
    print('Passed.')

def testTriangleArea():
    print('Testing triangleArea()... ', end='')
    assert(almostEqual(triangleArea(3,4,5), 6))
    assert(almostEqual(triangleArea(3,4,0), 0))
    assert(almostEqual(triangleArea(3,4,7), 0))
    assert(almostEqual(triangleArea(-3,-4,-5), 0))
    assert(almostEqual(triangleArea(1,2,2.8), (2.9 * 1.9 * 0.9 * 0.1)**0.5))
    print('Passed.')

def testTriangleAreaByCoordinates():
    print('Testing triangleAreaByCoordinates()... ', end='')
    assert(almostEqual(triangleAreaByCoordinates(1,1,9,1,5,5),16))
    assert(almostEqual(triangleAreaByCoordinates(0,0,10,0,0,50),250))
    assert(almostEqual(triangleAreaByCoordinates(1,3,5,3,3,(3+2*3**.5)),
                                                 4*3**.5))
    assert(almostEqual(triangleAreaByCoordinates(-6,7,-3,20,0,7),39))
    assert(almostEqual(triangleAreaByCoordinates(-2,2,2,-2,5,5),20))
    assert(almostEqual(triangleAreaByCoordinates(-2,2,-2,2,5,5),0))
    print('Passed.')

def testLineIntersection():
    print('Testing lineIntersection()... ', end='')
    assert(lineIntersection(2.5, 3, 2.5, 11) == None)
    assert(lineIntersection(25, 3, 25, 11) == None)
    # y=3x-5 and y=x+5 intersect at (5,10)
    assert(almostEqual(lineIntersection(3,-5,1,5), 5))
    # y=10x and y=-4x+35 intersect at (2.5,25)
    assert(almostEqual(lineIntersection(10,0,-4,35), 2.5))
    assert(almostEqual(lineIntersection(10,0,-4,15), 1.0714285714285714))
    print('Passed.')

def testThreeLinesArea():
    print('Testing threeLinesArea()... ', end='')
    assert(almostEqual(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert(almostEqual(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(almostEqual(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666666))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(almostEqual(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 25), 272.25))
    print('Passed.')

def testRectanglesOverlap():
    print('Testing rectanglesOverlap()...', end='')
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3,4,5,6) == False)
    print('Passed.')

#################################################
# testAll and main
#################################################

def testAll():
    testFabricYards()
    testFabricExcess()
    testIsEvenPositiveInt()
    testNthFibonacciNumber()
    testIsLegalTriangle()
    testIsRightTriangle()
    testTriangleArea()
    testTriangleAreaByCoordinates()
    testLineIntersection()
    testThreeLinesArea()
    testRectanglesOverlap()

def main():
    cs112_s22_week1_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
