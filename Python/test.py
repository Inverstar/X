# for i in range(0,2):
#     print(i)

# k=10000
# i=0
# while k > 1:
#     i+=1
#     print(i,k)
#     k=k/2

# for s in "PYTHON":
#     if s == "T":
#         continue
#     print(s,end="")

# def f(a,b):
#     a=4
#     return a+b

# def main():
#     a=5
#     b=6
#     print(f(a,b),a+b)  
# main()

# def func(a, b):
#     c = a**2 + b
#     b = a

# a=10
# b=100
# c=func(a, b)+a
# print(c, a, b)  # 输出：110 10 100

# import random

# def genpwd(length):
#     return "".join(str(random.randint(0, 9)) for _ in range(length))

# length = eval(input())
# random.seed(17)
# for i in range(3):
#     print(genpwd(length))

# import math

# def is_prime(n):
#     """判断一个数是否为质数"""
#     if n < 2:
#         return False
#     if n == 2:
#         return True  # 2 是唯一的偶数质数
#     if n % 2 == 0:
#         return False  # 排除偶数
#     for i in range(3, int(math.sqrt(n)) + 1, 2):  # 只检查奇数
#         if n % i == 0:
#             return False
#     return True

# # 获取用户输入，并转换为整数
# N = float(input())
# N = math.ceil(N)
# # 查找 5 个质数
# count = 0
# primes = []

# while count < 5:
#     if is_prime(N):
#         primes.append(str(N))
#         count += 1
#     N += 1

# # 按格式要求输出
# print(",".join(primes))

# d = {"a": 1, "a": 2, "c": 3}
# print(d["a"])   # 输出：2，因为字典中的键是唯一的，后面的值会覆盖前面的值


# s = "hello world"
# print(s.index("o"))  # 输出：4，返回第一个 "o" 的索引位置

import random

def genpwd(length):
    a = 10**(length-1)
    b = 10**length - 1
    print("生成的密码范围：", a, b)
    return "{}".format(random.randint(a, b))

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))