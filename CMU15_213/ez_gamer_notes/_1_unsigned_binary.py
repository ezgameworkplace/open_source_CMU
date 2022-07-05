'''
File:_1_unsigned_binary.py
Author:ezgameworkplace
Date:2022/6/23
Contact:hongzhang.ji@garena.com
'''

# 用str表达二进制 0000 1001

# binary to int

bin_str = '0110'
int_num = 90

def binary_2_decimal(bin_str:str)->int:
    int_num = int()
    count = len(bin_str)
    for index, b_str in enumerate(bin_str):
        if b_str == '1':
            int_num += 2**(count-index-1)
    return int_num

# int to binary
def decimal_2_binary(int_num:int)->str:
    bin_str = ''
    while int_num != 0:
        add_bin_str = str(int_num % 2)
        bin_str = bin_str + add_bin_str
        int_num //= 2
    return bin_str[::-1]

# print(binary_2_decimal(bin_str))
# print(decimal_2_binary(5))
# print(decimal_2_binary(3))
print(decimal_2_binary(600))

print(bin(600))


def dec2bin(num):
    l = []
    if num < 0:
        return '-' + dec2bin(abs(num))
    while True:
        num, remainder = divmod(num, 2)
        l.append(str(remainder))
        if num == 0:
            print(l)
            print(l[::-1])
            return ''.join(l[::-1])

print(dec2bin(600))