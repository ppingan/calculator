import math

# 计算阶乘
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# 计算arcsin(x)，返回角度
def arcsin_taylor(x):
    arcsin_x = 0
    for i in range(400):
        coef = factorial(2 * i) / ((4 ** i) * (factorial(i) ** 2) * (2 * i + 1))
        arcsin_x += coef * (x ** (2 * i + 1))
    return round(math.degrees(arcsin_x), 10)

# 主程序
while True:
    print("请选择要进行的操作：")
    print("1. arcsin")
    print("2. 退出")

    choice = input("请选择操作（输入数字）：")

    if choice == '1':
        x = float(input("请输入值（-1到1之间）："))
        if x < -1 or x > 1:
            print("输入值超出范围，请重新输入")
            continue
        result = arcsin_taylor(x)
        print("arcsin({:.4f}) = {:.10f}°".format(x, result))
    elif choice == '2':
        print("退出程序")
        break
    else:
        print("无效选择，请重新输入")
