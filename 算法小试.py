#楼梯问题
import time
#使用递归解决
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return f(n-1) + f(n-2)

#使用数据来缓存数据 , 用循环来遍历
def f1(n):
    asw = [0 for i in range(n+1)]
    asw[1] = 1
    asw[2] = 2

    for i in range(3,n+1):
        asw[i] = asw[i-1] + asw[i-2]
    return asw[n]

# 使用字典来缓存数据
asw = {}
asw[1] = 1
asw[2] = 2 

def f2(n):  
    if n > 2 and n not in asw.keys():
            asw[n] = f2(n-1) + f2(n-2)
    return asw[n]

print(f2(40))    




