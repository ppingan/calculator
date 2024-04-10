import math
import random


# 计算阶乘
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# 计算sin(x)，x为角度
def sin_taylor(x):
    # 将角度值转换为 -180 到 180 的范围内
    x %= 360
    if x > 180:
        x -= 360
    sin_x = 0
    x_rad = math.radians(x)
    for i in range(20):
        sign = (-1) ** i
        sin_x += sign * (x_rad ** (2 * i + 1)) / factorial(2 * i + 1)
    return round(sin_x, 10)


# 测试函数
def test_trig_functions(num_tests):
    total_error = 0
    for _ in range(num_tests):
        # 生成随机角度值
        angle = random.uniform(-180, 180)

        # 使用math库计算sin值
        sin_result = round(math.sin(math.radians(angle)), 10)

        # 使用泰勒公式计算sin值
        sin_approx = sin_taylor(angle)

        # 计算误差
        sin_error = abs(sin_result - sin_approx)

        # 输出结果
        print("角度值: {:.4f}".format(angle))
        print("Sin(math库): {:.10f}".format(sin_result))
        print("Sin(泰勒公式): {:.10f}".format(sin_approx))
        print("误差: {:.10f}".format(sin_error))
        print("-----------------------------------------")

        # 累加误差
        total_error += sin_error

    # 计算平均误差
    average_error = total_error / num_tests
    print("平均误差: {:.10f}".format(average_error))


# 主程序
num_tests = int(input("请输入要进行的测试次数："))
test_trig_functions(num_tests)
