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

# 测试函数
def test_trig_functions():
    while True:
        print("请选择要测试的三角函数：")
        print("1. arctan")
        print("2. 退出")

        choice = input("请选择操作（输入数字）：")
        if choice == '1':
            value = float(input("请输入值："))
            arctan_result = round(math.degrees(math.atan(value)), 10)
            arctan_approx = arctan_taylor(value)
            arctan_error = abs(arctan_result - arctan_approx)
            print("Arctan(math库): {:.10f}".format(arctan_result))
            print("Arctan(泰勒公式): {:.10f}".format(arctan_approx))
            print("误差: {:.10f}".format(arctan_error))
            if arctan_error < 0.0001:
                print("计算器设计无误！")
            else:
                print("计算器设计存在误差，请检查！")
        elif choice == '2':
            print("退出程序")
            break
        else:
            print("无效选择，请重新输入")


# 主程序
test_trig_functions()
