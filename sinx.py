import math

# 计算阶乘
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# 计算sin(x)，其中x以度为单位
def sin_taylor(x):
    x %= 360
    if x > 180:
        x -= 360
    sin_x = 0
    x_rad = math.radians(x)
    for i in range(20):
        sign = (-1) ** i
        sin_x += sign * (x_rad ** (2 * i + 1)) / factorial(2 * i + 1)
    return round(sin_x, 10)

# 主程序
while True:
    print("选择要计算的三角函数：")
    print("1. sin")
    print("5. 退出")

    choice = input("选择操作（输入数字）：")

    if choice == '1':
        angle = float(input("输入角度值："))
        result = sin_taylor(angle)
        print("sin({:.2f}°) = {:.10f}".format(angle, result))
    elif choice == '5':
        print("退出程序。")
        break
    else:
        print("无效选择，请重新输入。")
