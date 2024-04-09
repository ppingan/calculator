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


while True:
    print("请选择要测试的三角函数：")
    print("1. arcsin")
    print("2. 退出")

    choice = input("请选择操作（输入数字）：")

    if choice == '1':
        value = float(input("请输入值（-1到1之间）："))
        if value < -1 or value > 1:
            print("输入值超出范围，请重新输入")
            continue
        arcsin_result = round(math.degrees(math.asin(value)), 10)
        arcsin_approx = arcsin_taylor(value)
        arcsin_error = abs(arcsin_result - arcsin_approx)
        print("Arcsin(math库): {:.10f}°".format(arcsin_result))
        print("Arcsin(泰勒公式): {:.10f}°".format(arcsin_approx))
        print("误差: {:.10f}".format(arcsin_error))
        if arcsin_error < 0.0001:
            print("误差小于0.0001，计算器设计无误！")
        else:
            print("计算器设计存在误差，请检查！")
    elif choice == '2':
        print("退出程序")
        break
    else:
        print("无效选择，请重新输入")



