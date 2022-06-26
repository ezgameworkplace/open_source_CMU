#-*- codeing = utf-8 -*-
'''
@File : notes.py
@Time : 2022/4/1 16:15
@Author : ezgameworkplace
'''
# THIS CODE STILL HAS A BUG (ON PURPOSE)!!!!

# When you run it, it will hang (run forever)!!!!

def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

def nthPrime(n):
    found = 0
    guess = 0
    while (found <= n):
        print(locals()) ### <--- THIS is our well-placed print statement!
        input()         ### <--- THIS pauses until we hit Enter. Sweet!
        guess += 1
        if (isPrime(guess)):
            found += 1
    return guess

# print('The next line will hang (run forever):')
# print(nthPrime(5))

def digitCount(n):
    # use loop, for unknown length of loop, we use while statement
    n = abs(n)
    if n == 0: return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def reverse(n): #求一个数字的倒序
    digit = None
    result = 0
    while n > 0:
        digit = n % 10
        n //= 10
        result = (result*10) + digit
    return result

def rotate(n): #把第一位和最后一位切换，其余位依次切换
    if n == 0: return 0
    rev = reverse(n)
    last_digit = rev % 10 #旋转后的最后一位就是倒序的最后一位
    start_digits = reverse(rev//10)*10#旋转后的前部分就是倒序整除10后的倒序再乘以10
    return start_digits + last_digit




def isRotation(x, y):
    if x==y: return True
    for i in range(digitCount(x)):
        x=rotate(x)
        if(x==y): return True
    return False

# print(isRotation(1234, 4123))


def h(n):
    return n+5
def f(g, x):
    return 2*g(x)
# print(f(h,h(5))) # prints 16


x = 376
y = 0
digit_x = int()
digit_y = int()
new_digit = int()
sum = int()
count = 0
while x != 0:
    digit_x = x % 10
    digit_y = y % 10
    new_digit = digit_y + digit_x
    x //= 10
    if y > 0:
        y //= 10
        if new_digit > 9:
            new_digit = new_digit % 10 #如果比9大就保存个位数
    else:
        pass
    sum = sum + new_digit * (10 ** count)
    count += 1
print(sum)
