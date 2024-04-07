import math

# 定义泰勒级数的项数
TERMS = 4000000

# 计算阶乘
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# 计算arctan(x)，返回角度
def arctan_taylor(x):
    arctan_x = 0
    for i in range(TERMS):
        coef = (-1) ** i
        arctan_x += coef * (x ** (2 * i + 1)) / (2 * i + 1)
    return round(math.degrees(arctan_x), 10)

# 主程序
while True:
    print("请选择要计算的三角函数：")
    print("1. arctan")
    print("2. 退出")

    choice = input("请选择操作（输入数字）：")

    if choice == '1':
        x = float(input("请输入值："))
        result = arctan_taylor(x)
        print("arctan({:.2f}) = {:.10f}°".format(x, result))
    elif choice == '2':
        print("退出程序")
        break
    else:
        print("无效选择，请重新输入")
