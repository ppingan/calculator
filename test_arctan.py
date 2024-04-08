import math

# 计算阶乘
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# 使用牛顿迭代法计算arctan(x)，初始猜测值为0，迭代次数为n
def arctan_newton(x, n=1000000):
    if x == 0:
        return 0

    # 初始猜测值为0
    guess = 0

    # 迭代n次
    for _ in range(n):
        guess = guess + (math.atan(x) - guess) / (1 + x ** 2)

    # 将弧度转换为角度并返回
    return round(math.degrees(guess), 10)

while True:
    print("请选择要测试的三角函数：")
    print("1. arctan")
    print("2. 退出")

    choice = input("请选择操作（输入数字）：")
    if choice == '1':
        value = float(input("请输入值："))
        arctan_result = round(math.degrees(math.atan(value)), 10)
        arctan_approx = arctan_newton(value)
        arctan_error = abs(arctan_result - arctan_approx)
        print("Arctan(math库): {:.10f}°".format(arctan_result))
        print("Arctan(泰勒公式): {:.10f}°".format(arctan_approx))
        print("误差: {:.10f}°".format(arctan_error))
        if arctan_error < 0.0001:
            print("计算器设计无误！")
        else:
            print("计算器设计存在误差，请检查！")
    elif choice == '2':
        print("退出程序")
        break
    else:
        print("无效选择，请重新输入")




