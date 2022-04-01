#-*- codeing = utf-8 -*-
'''
@File : quiz1.py
@Time : 2022/3/23 11:40
@Author : ezgameworkplace
'''

def f(x):
    print(f'f({x})')
    x += 1
    return x**2//10

def g(x):
    print(f'g({x})')
    x = (7*x)%5
    return f(x+3)

def ct1(x):
    print(f(g(f(x))) + x)

# print(ct1(5)) # hint: prints 6 total lines
#1.print:f(5) return:3
#2.print:g(3) return:f(1+3)
#3.print:f(4) return:2
#4.print:f(2) return:0
#5.print:5
#6.print:None --print无返回值的函数返回值默认是None

def p(a, b):
    return (abs(a - b) + abs(b - a)) if (a != b) else a*b

def q(a, b, c):
    if (a > b):
        return p(a, b+c)
    a += b
    if (a > c):
        return p(a+b, c)
    else:
        c %= b
        return p(a+c, b)

def ct2(a, b, c):
    print(q(a, b, c))
    print(q(b, c, a))
    print(q(c, a, b))

# ct2(3, 5, 2) # hint: prints 3 total lines

# Note: almostEqual(x, y) and roundHalfUp(n) are both supplied for you. On all
#   quizzes, you may write additional helper functions if you wish.
def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))
#---------------

def return_digits(n):
    n1 = n % 10
    n2 = n // 10 % 10
    n3 = n // 100 % 10
    return n1, n2, n3

def return_near(n):
    last = n - 1
    next = n + 1
    return last, next

def is_factor(n, m):
    if n > 0:
        if m % n == 0:
            return True
        else:
            return False
    else:
        return False

#Write your function here:
def isNearlyFactorish(n):
    if isinstance(n, int):
        if 100 <= n <= 999:
            n1, n2, n3 = return_digits(n)
            if n1 > 0 and n2 > 0 and n3 > 0:
                n1_0, n1_1 = return_near(n1)
                n2_0, n2_1 = return_near(n2)
                n3_0, n3_1 = return_near(n3)
                print(locals())
                input()
                if is_factor(n1_0, n) or is_factor(n1_1, n):
                    if is_factor(n2_0, n) or is_factor(n2_1, n):
                        if is_factor(n3_0, n) or is_factor(n3_1, n):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False



# We have provided these test cases:
def testIsNearlyFactorish():
    print('Testing isNearlyFactorish()...', end='')
    assert(isNearlyFactorish(152) == True)
    assert(isNearlyFactorish(264) == False)
    assert(isNearlyFactorish(130) == False)   # 0 is not positive
    assert(isNearlyFactorish(1234) == False)  # too big
    assert(isNearlyFactorish(12) == False)    # too small
    assert(isNearlyFactorish(-124) == False)  # ditto
    assert(isNearlyFactorish(124.0) == False) # not an integer
    assert(isNearlyFactorish('ack') == False) # ditto

    # we added a few more test cases after the quiz
    # to help with your Fix-It Friday submission:
    assert(isNearlyFactorish(153) == False)
    assert(isNearlyFactorish(-152) == False)
    assert(isNearlyFactorish(140) == False)
    assert(isNearlyFactorish(-140) == False)

    print('Passed!')

# testIsNearlyFactorish()

#bonus question
def f(x): return x+5
def g(x): return f(x-3)
def h(x): return g(g(x)%f(x))
def bonusCt1(f, g, x):
    # print(locals())
    # input()
    if (x > 0):
        print(x)
        print(-f(x))
        return bonusCt1(g, h, -f(x)) #这里的f实际上是g函数,g实际上是f，h依然是h
    else:
       return f(g(h(x)))
print(-f(4))
print(bonusCt1(g, f, 4))
#推算：b(g,f,4) —— b(f,h,-g(x)) —— b(f,h,-6) —— f(h(h(-6))
#第一步，return的b中的参数g变成了f，h不变，-f(x)变成了-g(x)
#第二步，-g(x)带入x=4可求出-6
#第三步，return的f(g(h(x)))中的g被h替换了
#总结，貌似函数的参数是一个函数的时候，是可以被其他函数替换的，而如果不替换，则使用默认的函数作为参数
#NOTES：mod在python中向下取整做模运算，既商取接近于-infinite