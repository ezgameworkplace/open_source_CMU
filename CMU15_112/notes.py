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
            found + 1
    return guess

# print('The next line will hang (run forever):')
# print(nthPrime(5))

print(abs(-31//10))