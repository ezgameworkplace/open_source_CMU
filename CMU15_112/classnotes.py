'''
File:classnotes.py
Author:ezgameworkplace
Date:2022/3/27
Contact:hongzhang.ji@garena.com
'''



def eratosthenes(n):# 埃拉托斯特尼筛法/素数筛
    IsPrime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1): #从2到最大的平方约数，平方约数就是两个最近的公约数
        if IsPrime[i]:
            print(i)
            print(IsPrime[i])
            for j in range(i * i, n + 1, i): #去掉2的倍数去掉3的倍数去掉。。。
                IsPrime[j] = False
    return [x for x in range(2, n + 1) if IsPrime[x]]


if __name__ == "__main__":
    print(eratosthenes(24))