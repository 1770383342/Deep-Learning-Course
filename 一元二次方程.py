import math

print("求一元二次方程 ax^2 + bx + c = 0 的值")
a = float(input("请输入a的值 a = "))
b = float(input("请输入b的值 b = "))
c = float(input("请输入c的值 c = "))
t = b * b - 4 * a * c
if t > 0:
    x1 = (-b + math.sqrt(t)) / (2 * a)
    x2 = (-b - math.sqrt(t)) / (2 * a)
    print("函数有两个根 x1 = ", x1, " x2 = ", x2)
elif t == 0:
    x = (-b + math.sqrt(t)) / (2 * a)
    print("函数有一个根 x = ", x)
else:
    print("函数无解")