#读入n（1 <= n <= 10000）个整数，求它们的和与均值。
#110918e880c29cd275aa593df696e4fc81e082ee6ff2929651fb656a7c634665
n = int(input())
k = 0
for x in range(n):
    k += int(input())
print(k,end=' ')
print("%.5f"%(k/n))