#################################################
# hw1.py
# name:
# andrew id:
#################################################

import cs112_s22_week1_linter
import math

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Part A
#################################################

def distance(x1, y1, x2, y2):
    '''
    Write the function distance(x1, y1, x2, y2) that takes four int or float values x1, y1, x2, y2 that represent the two points (x1, y1) and (x2, y2), and returns the distance between those points as a float.
    '''
    width = abs(x1-x2)
    height = abs(y1-y2)
    distance = (width**2+height**2)**(1/2)
    return distance

def circlesIntersect(x1, y1, r1, x2, y2, r2):
    '''Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) that takes 6 numbers (ints or floats) -- x1, y1, r1, x2, y2, r2 -- that describe the circle centered at (x1,y1) with radius r1, and the circle centered at (x2,y2) with radius r2, and returns True if the two circles intersect and False otherwise.'''
    distance_btw_center = distance(x1,y1,x2,y2)
    intersect_distance = r1 + r2
    if distance_btw_center <= intersect_distance:
        return True
    else:
        return False


def getInRange(x, bound1, bound2):
    '''Write the function getInRange(x, bound1, bound2) which takes 3 int or float values -- x, bound1, and bound2, where bound1 is not necessarily less than bound2. If x is between the two bounds, just return it unmodified. Otherwise, if x is less than the lower bound, return the lower bound, or if x is greater than the upper bound, return the upper bound.'''
    lower_bound = min(bound1, bound2)
    upper_bound = max(bound1, bound2)
    if lower_bound<=x<=upper_bound:
        return x
    elif x<lower_bound:
        return lower_bound
    else:
        return upper_bound


def eggCartons(eggs):
    '''
    Write the function eggCartons(eggs) that takes a non-negative integer number of eggs, and returns the smallest integer number of cartons required to hold that many eggs, where a carton may hold up to 12 eggs.
    '''
    if eggs%12 == 0:
        cartons = (eggs//12)
    else:
        cartons = (eggs//12) + 1
    return cartons

def pascalsTriangleValue(row, col):
    '''
    用组合通用公式：n!/k!(n-k)!
    n是行，k是列
    n choose k
    '''
    if row >= 0 and col >= 0 and row >= col:
        import math
        result = math.factorial(row)/(math.factorial(col)*math.factorial(row-col))
        return result
    else:
        return None

def getKthDigit(n, k):
    '''
    Write the function getKthDigit(n, k) that takes a possibly-negative int n and a non-negative int k, and returns the kth digit of n, starting from 0, counting from the right.
    '''
    print(n)
    n = abs(n)
    result = n//10**k % 10
    return result

def setKthDigit(n, k, d):
    '''
    Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d -- where n is a possibly-negative int, k is a non-negative int, and d is a non-negative single digit (between 0 and 9 inclusive). This function returns the number n with the kth digit replaced with d. Counting starts at 0 and goes right-to-left, so the 0th digit is the rightmost digit.
    '''
    if n >= 0:
        sign = 1
    else:
        sign = -1
    n = abs(n)
    rank = getKthDigit(n, k)
    result = n+(d-rank)*10**k
    return result if sign == 1 else -result

#################################################
# Part B
#################################################
        
def nearestOdd(n):
    """Write the function nearestOdd(n) that takes an int or float n, and returns as an int value the nearest odd number to n. In the case of a tie, return the smaller odd value. Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.

Hint: Remember that the built-in round function works in surprising ways. Instead of round(n), you should use roundHalfUp(n) from this week's notes. That said, there are good ways to solve this problem without using rounding at all, if you prefer."""
    result = roundHalfUp(n)
    if result % 2 == 0:
        if n - result > 0:
            result += 1
            return result
        else:
            result -= 1
            return result
    else:
        return result

def numberOfPoolBalls(rows):
    """
    Triangular number
    n*(n+1)/2
    """
    result = rows*(rows+1)/2
    return result

def numberOfPoolBallRows(balls):
    """
    smallest int number of rows required for the given number of pool balls.
    知道球数，求最少需要多少row组成
    T_n为行数，x为球数
    T_n = ((8x+1)**(1/2)-1)/2
    """
    result = ((8*balls+1)**(1/2)-1)/2
    import decimal
    rounding = decimal.ROUND_CEILING
    result = int(decimal.Decimal(result).to_integral_value(rounding=rounding))
    return result

def colorBlender(rgb1, rgb2, midpoints, n):
    """
    找两个颜色之间的颜色，用纯int表达rgb
    :param rgb1:
    :param rgb2:
    :param midpoints: 区间的个数
    :param n: 用于返回第n个区间的颜色rgb
    :return:
    """
    mid_intervals = midpoints + 1
    if 0 <= n <= mid_intervals:
        rgb1_red = rgb1//(10**6)
        rgb1_green = (rgb1 - rgb1_red*10**6)//(10**3)
        rgb1_blue = rgb1 - rgb1_red*10**6 - rgb1_green*10**3
        rgb2_red = rgb2//(10**6)
        rgb2_green = (rgb2 - rgb2_red*10**6)//(10**3)
        rgb2_blue = rgb2 - rgb2_red*10**6 - rgb2_green*10**3
        difference_red = abs((rgb1_red - rgb2_red)/mid_intervals)
        difference_green = abs((rgb1_green - rgb2_green)/mid_intervals)
        difference_blue = abs((rgb1_blue - rgb2_blue)/mid_intervals)
        if rgb1_red > rgb2_red:
            result_red = rgb1_red-difference_red*n
        else:
            result_red = rgb1_red+difference_red*n
        if rgb1_green > rgb2_green:
            result_green = rgb1_green-difference_green*n
        else:
            result_green = rgb1_green+difference_green*n
        if rgb1_blue > rgb2_blue:
            result_blue = rgb1_blue-difference_blue*n
        else:
            result_blue = rgb1_blue+difference_blue*n
        result_red = roundHalfUp(result_red)
        result_green = roundHalfUp(result_green)
        result_blue = roundHalfUp(result_blue)
        result = result_red*10**6 + result_green*10**3 + result_blue
        return result
    else:
        return None

#################################################
# Bonus/Optional
#################################################

def handToDice(hand):
    one = getKthDigit(hand, 0)
    ten = getKthDigit(hand, 1)
    hundred = getKthDigit(hand, 2)
    return (hundred, ten, one)

def dice_has_same(x,y,z):
    if x==y and x==z:
        return x, y, z, True
    elif x==y:
        return x, y, True
    elif x==z:
        return x, z, True
    elif y==z:
        return y, z, True
    else:
        return None, False

def diceToOrderedHand(x, y, z):
    n = 000
    min_dice = min(x,y,z)
    max_dice = max(x,y,z)
    if dice_has_same(x,y,z) == (x, y, True) or dice_has_same(x,y,z) == (x, z, True):
        mid_dice = x
    elif dice_has_same(x,y,z) == (y, z, True):
        mid_dice = y
    else:
        if x != min_dice and x != max_dice:
            mid_dice = x
        elif y != min_dice and y != max_dice:
            mid_dice = y
        else:
            mid_dice = z
    n = setKthDigit(n, 0, min_dice)
    n = setKthDigit(n, 1, mid_dice)
    n = setKthDigit(n, 2, max_dice)
    return n


def playStep2(hand, dice):
    """
    1.  Roll 3 dice.
    2.  If you do not have 3 matching dice:
        If you have 2 matching dice (a pair), keep the pair and roll one die to replace the third die.
        Otherwise, if you have no matching dice, keep the highest die and roll two dice to replace the other two dice.
    hand是手头的dice(三位数)，dice是模拟又投出的点数(投出的顺序从右往左)
    """
    one = getKthDigit(hand, 0)
    ten = getKthDigit(hand, 1)
    hundred = getKthDigit(hand, 2)
    if dice_has_same(one, ten, hundred) == (one, ten, hundred, True):
        result = diceToOrderedHand(one, ten, hundred), dice
    elif dice_has_same(one, ten, hundred) == (one, ten, True):
        new_hundred = getKthDigit(dice, 0)
        result = diceToOrderedHand(one, ten, new_hundred), dice//10
    elif dice_has_same(one, ten, hundred) == (one, hundred, True):
        new_ten = getKthDigit(dice, 0)
        result = diceToOrderedHand(one, new_ten, hundred), dice//10
    elif dice_has_same(one, ten, hundred) == (ten, hundred, True):
        new_one = getKthDigit(dice, 0)
        result = diceToOrderedHand(new_one, ten, hundred), dice//10
    else:
        my_highest_dice = max(one, ten, hundred)
        new_one = getKthDigit(dice, 0)
        new_ten = getKthDigit(dice, 1)
        result = diceToOrderedHand(my_highest_dice, new_one, new_ten), dice//10**2
    return result


def score(hand):
    one = getKthDigit(hand, 0)
    ten = getKthDigit(hand, 1)
    hundred = getKthDigit(hand, 2)
    if dice_has_same(one, ten, hundred)==(one,ten,hundred,True):
        return 20 + one + ten + hundred
    elif dice_has_same(one, ten, hundred)==(one, ten, True):
        return 10 + one + ten
    elif dice_has_same(one, ten, hundred)==(one, hundred, True):
        return 10 + one + hundred
    elif dice_has_same(one, ten, hundred)==(ten, hundred, True):
        return 10 + ten + hundred
    else:
        return max(one, ten, hundred)


def bonusPlayThreeDiceYahtzee(dice):
    x, y, z = handToDice(dice)
    my_dice_on_hand = diceToOrderedHand(x,y,z)
    dice_left = dice//10**3
    my_dice_on_hand, dice_left = playStep2(my_dice_on_hand, dice_left)
    my_dice_on_hand, dice_left = playStep2(my_dice_on_hand, dice_left)
    return my_dice_on_hand,score(my_dice_on_hand)


def bonusFindIntRootsOfCubic(a, b, c, d):
    '''
    The solution of ax3+bx2+cx+d=0 ： https://math.vanderbilt.edu/schectex/courses/cubic/
    找到一个整数根后，转化成二次方程组 ：  https://en.wikipedia.org/w/index.php?title=Cubic_function&oldid=916994377#Factorization
    '''
    p = -b/(3*a)
    q = p**3+(b*c-3*a*d)/(6*a**2)
    r = c/(3*a)
    # imaginary=(q**2+(r-p**2)**3)**(1/2)
    # imaginaryPart=imaginary-imaginary.real
    # m=q+imaginaryPart
    # n=q-imaginaryPart
    # x1=m**(1/3)+n**(1/3)+p
    # x1 = int(x1.real)
    # print('x1', x1)
    # x2=(-b-x1*a+(b**2-4*a*c-2*a*b*x1-3*a**2*x1**2)**.5)/(2*a)
    # x3=(-b-x1*a-(b**2-4*a*c-2*a*b*x1-3*a**2*x1**2)**.5)/(2*a)
    x_1 = (q+(q**2+(r-p**2)**3)**(1/2))**(1/3)+(q-(q**2+(r-p**2)**3)**(1/2))**(1/3)+p
    x_1 = int(x_1.real)
    print('x_1',x_1)
    x_2 = (-b-x_1*a+(b**2-4*a*c-2*a*b*x_1-3*a**2*x_1**2)**.5)/(2*a)
    x_2 = int(x_2.real)
    x_3 = (-b-x_1*a-(b**2-4*a*c-2*a*b*x_1-3*a**2*x_1**2)**.5)/(2*a)
    x_3 = int(x_3.real)
    x_min = min(x_1, x_2, x_3)
    x_max = max(x_1, x_2, x_3)
    x_mid = x_1+x_2+x_3-x_min-x_max
    # x_min = min(x1, x2, x3)
    # x_max = max(x1, x2, x3)
    # x_mid = x1+x2+x3-x_min-x_max
    print('myansw',x_min, x_mid, x_max)
    return x_min, x_mid, x_max

#################################################
# Test Functions
#################################################

def testDistance():
    print('Testing distance()... ', end='')
    assert(almostEqual(distance(0, 0, 3, 4), 5))
    assert(almostEqual(distance(-1, -2, 3, 1), 5))
    assert(almostEqual(distance(-.5, .5, .5, -.5), 2**0.5))
    print('Passed!')

def testCirclesIntersect():
    print('Testing circlesIntersect()... ', end='')
    assert(circlesIntersect(0, 0, 2, 3, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 4, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 5, 0, 2) == False)
    assert(circlesIntersect(3, 3, 3, 3, -3, 3) == True)
    assert(circlesIntersect(3, 3, 3, 3,- 3, 2.99) == False)
    print('Passed!')

def testGetInRange():
    print('Testing getInRange()... ', end='')
    assert(getInRange(5, 1, 10) == 5)
    assert(getInRange(5, 5, 10) == 5)
    assert(getInRange(5, 9, 10) == 9)
    assert(getInRange(5, 10, 10) == 10)
    assert(getInRange(5, 10, 1) == 5)
    assert(getInRange(5, 10, 5) == 5)
    assert(getInRange(5, 10, 9) == 9)
    assert(getInRange(0, -20, -30) == -20)
    assert(almostEqual(getInRange(0, -20.25, -30.33), -20.25))
    print('Passed!')

def testEggCartons():
    print('Testing eggCartons()... ', end='')
    assert(eggCartons(0) == 0)
    assert(eggCartons(1) == 1)
    assert(eggCartons(12) == 1)
    assert(eggCartons(13) == 2)
    assert(eggCartons(24) == 2)
    assert(eggCartons(25) == 3)
    print('Passed!')

def testPascalsTriangleValue():
    print('Testing pascalsTriangleValue()... ', end='')
    assert(pascalsTriangleValue(3,0) == 1)
    assert(pascalsTriangleValue(3,1) == 3)
    assert(pascalsTriangleValue(3,2) == 3)
    assert(pascalsTriangleValue(3,3) == 1)
    assert(pascalsTriangleValue(1234,0) == 1)
    assert(pascalsTriangleValue(1234,1) == 1234)
    assert(pascalsTriangleValue(1234,2) == 760761)
    assert(pascalsTriangleValue(3,-1) == None)
    assert(pascalsTriangleValue(3,4) == None)
    assert(pascalsTriangleValue(-3,2) == None)
    print('Passed!')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed!')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed!')

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    # results must be int's not floats
    assert(isinstance(nearestOdd(13.0), int))
    assert(isinstance(nearestOdd(11.999), int))
    print('Passed!')

def testNumberOfPoolBalls():
    print('Testing numberOfPoolBalls()... ', end='')
    assert(numberOfPoolBalls(0) == 0)
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 3)   # 1+2 == 3
    assert(numberOfPoolBalls(3) == 6)   # 1+2+3 == 6
    assert(numberOfPoolBalls(10) == 55) # 1+2+...+10 == 55
    print('Passed!')

def testNumberOfPoolBallRows():
    print('Testing numberOfPoolBallRows()... ', end='')
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    print('Passed!')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed!')

def testBonusPlayThreeDiceYahtzee():
    print('Testing bonusPlayThreeDiceYahtzee()...', end='')
    assert(handToDice(123) == (1,2,3))
    assert(handToDice(214) == (2,1,4))
    assert(handToDice(422) == (4,2,2))
    assert(diceToOrderedHand(1,2,3) == 321)
    assert(diceToOrderedHand(6,5,4) == 654)
    assert(diceToOrderedHand(1,4,2) == 421)
    assert(diceToOrderedHand(6,5,6) == 665)
    assert(diceToOrderedHand(2,2,2) == 222)
    assert(playStep2(413, 2312) == (421, 23))
    assert(playStep2(421, 23) == (432, 0))
    assert(playStep2(413, 2345) == (544, 23))
    assert(playStep2(544, 23) == (443, 2))
    assert(playStep2(544, 456) == (644, 45))
    assert(score(432) == 4)
    assert(score(532) == 5)
    assert(score(443) == 10+4+4)
    assert(score(633) == 10+3+3)
    assert(score(333) == 20+3+3+3)
    assert(score(555) == 20+5+5+5)
    assert(bonusPlayThreeDiceYahtzee(2312413) == (432, 4))
    assert(bonusPlayThreeDiceYahtzee(2315413) == (532, 5))
    assert(bonusPlayThreeDiceYahtzee(2345413) == (443, 18))
    assert(bonusPlayThreeDiceYahtzee(2633413) == (633, 16))
    assert(bonusPlayThreeDiceYahtzee(2333413) == (333, 29))
    assert(bonusPlayThreeDiceYahtzee(2333555) == (555, 35))
    print('Passed!')

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    print('myabcd', a,b, c,d)
    result1, result2, result3 = bonusFindIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    print('real',actual)
    assert(almostEqual(m1, result1))
    assert(almostEqual(m2, result2))
    assert(almostEqual(m3, result3))

def testBonusFindIntRootsOfCubic():
    print('Testing bonusFindIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # Part A:
    #testDistance()
    #testCirclesIntersect()
    #testGetInRange()
    # testEggCartons()
    # testPascalsTriangleValue()
    # testGetKthDigit()
    # testSetKthDigit()
    # # Part B:
    # testNearestOdd()
    # testNumberOfPoolBalls()
    # testNumberOfPoolBallRows()
    # testColorBlender()
    # # Bonus:
    # testBonusPlayThreeDiceYahtzee()
    testBonusFindIntRootsOfCubic()

def main():
    cs112_s22_week1_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
