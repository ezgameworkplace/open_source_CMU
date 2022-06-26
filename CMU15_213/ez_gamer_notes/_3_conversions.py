'''
File:_3_conversions.py
Author:ezgameworkplace
Date:2022/6/26
Contact:hongzhang.ji@garena.com
'''
# hexadecimal to binary and decimal

bin_str = '1100100101111011'
int_num = int()
hex_str = ''

def binary_2_hexadecimal(bin_str:str)->str:
    '''
    把二进制转化成十进制，再参考十进制对应的十六进制，换算成十六进制
    :param bin_str:
    :return:
    '''
    bin_length = len(bin_str)
    remainder = bin_length % 4
    if remainder != 0:
        bin_str = '0' * remainder + bin_str
    byte_list = []
    byte = ''
    for index, bit in enumerate(bin_str):
        byte +=  bit
        if (index+1) % 4 == 0:
            byte_list.append(byte)
            byte = ''

    # 单独的映射
    decimal_list = []
    for byte in byte_list:
        from _1_unsigned_binary import binary_2_decimal
        decimal_list.append(binary_2_decimal(byte))

    hexadecimal_str = '0123456789ABCDEF'
    my_hexadecimal = ''
    for decimal in decimal_list:
        hexadecimal = hexadecimal_str[decimal]
        my_hexadecimal += hexadecimal

    return '0x' + my_hexadecimal


def decimal_2_hexadecimal(int_num:int)->str:
    # x = q*16 + r
    hexadecimal_str = '0123456789ABCDEF'
    my_hexadecimal = ''
    if int_num % 16 == 0:
        remainder = int_num % 16
        hexa_remainder = hexadecimal_str[remainder]
        my_hexadecimal += hexa_remainder
        int_num //= 16
    while int_num % 16 != 0:
        remainder = int_num % 16
        hexa_remainder = hexadecimal_str[remainder]
        my_hexadecimal += hexa_remainder
        int_num //= 16
    return '0x' + my_hexadecimal[::-1]

print(binary_2_hexadecimal('1100100101111011'))
print(decimal_2_hexadecimal(3200))
