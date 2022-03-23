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

print(ct1(5)) # hint: prints 6 total lines
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

ct2(3, 5, 2) # hint: prints 3 total lines