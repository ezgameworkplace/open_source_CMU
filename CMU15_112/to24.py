'''
File:to24.py
Author:ezgameworkplace
Date:2022/6/8
Contact:hongzhang.ji@garena.com
'''

# 给四个数字能否组成另外一个数字

def sumNumber(num1, num2):
    print('%s+%s' % (num1,num2))
    return num1+num2

def differenceNumber(num1, num2):
    print('%s-%s' % (num1,num2))
    return num1-num2

def productNumber(num1, num2):
    print('*')
    return num1*num2

def fractionNumber(num1, num2):
    print('/')
    return num1/num2

def allCaseNumber(num1, num2):
    _sum = sumNumber(num1, num2)
    _difference = differenceNumber(num1, num2)
    _product = productNumber(num1, num2)
    _fraction = fractionNumber(num1, num2)
    result = [_sum, _difference, _product, _fraction]
    return result

def toNumber(num1, num2, result):
    number_list = allCaseNumber(num1, num2)
    if result in number_list:
        return True
    else:
        return False

def toNumberList(number_list, result):
    if len(number_list) == 1:
        if number_list[0] == result:
            return True
        else:
            return False
    else:
        for number in number_list:
            new_number_list = allCaseNumber(number, result)
            number_list.remove(number)
            for new_number in new_number_list:
                toNumberList(number_list, new_number)

from typing import List
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        TARGET = 24
        EPSILON = 1e-6
        ADD, MULTIPLY, SUBTRACT, DIVIDE = 0, 1, 2, 3

        def solve(nums: List[float]) -> bool:
            if not nums:
                return False
            if len(nums) == 1:
                return abs(nums[0] - TARGET) < EPSILON
            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if i != j:
                        newNums = list()
                        for k, z in enumerate(nums):
                            if k != i and k != j:
                                newNums.append(z)
                        for k in range(4):
                            if k < 2 and i > j:
                                continue
                            if k == ADD:
                                newNums.append(x + y)
                            elif k == MULTIPLY:
                                newNums.append(x * y)
                            elif k == SUBTRACT:
                                newNums.append(x - y)
                            elif k == DIVIDE:
                                if abs(y) < EPSILON:
                                    continue
                                newNums.append(x / y)
                            if solve(newNums):
                                return True
                            newNums.pop()
            return False

        return solve(nums)
mylist=[2,2,4]
mysol = Solution()
# print(mysol.judgePoint24(mylist))

#如何改变参数的类型来递归（重载？）
#我想对一个list中的每一个int做递归，递归一次出现一个list，在对这个list中的int递归