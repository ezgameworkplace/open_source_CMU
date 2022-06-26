'''
File:_2_signed_binary.py
Author:ezgameworkplace
Date:2022/6/23
Contact:hongzhang.ji@garena.com
'''
# Two's complement
# 用str表达二进制 0000 1001

# binary to int

# bin_str = '11110111'
# int_num = int()
# count = len(bin_str)
# for index, b_str in enumerate(bin_str):
#     if index == 0:
#         if b_str == '1':
#             int_num += - 2**(count-index-1)
#     else:
#         if b_str == '1':
#             int_num += 2**(count-index-1)
#
# print(int_num)


# int to binary
bin_str = ''
int_num = -9
count = 0
while int_num != 0:
    if int_num < 0:
        int_num *= -1
    count += 1
    add_bin_str = str(int_num % 2)
    bin_str = bin_str + add_bin_str
    int_num //= 2

signed_bin_str = ''
for index, str_num in enumerate(bin_str):
    if index != len(bin_str)-1:
        if str_num == '0':
            signed_bin_str += '1'
        else:
            signed_bin_str += '0'
    else:
        signed_bin_str += '1'

    print(signed_bin_str)