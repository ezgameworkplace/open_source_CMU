'''
File:_1_unsigned_binary.py
Author:ezgameworkplace
Date:2022/6/23
Contact:hongzhang.ji@garena.com
'''

# 用str表达二进制 0000 1001

# binary to int

bin_str = '1100100101111011'
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
    return bin_str

print(binary_2_decimal(bin_str))
print(decimal_2_binary(51579))