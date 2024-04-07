
#计算阶乘
def jiecheng(n):
    if n == 0:
        return 1
    else:
        return n * jiecheng(n - 1)

#将角度转化为弧度
def convert_degrees_to_radians(degrees):
    # 定义一个近似π的值
    PI = 3.141592653589793
    return degrees * (PI / 180)

#通过泰勒展开式求cos函数的近似值,输入为角度
def cos(x_degree):
    x_degree = x_degree % 360
    #print(xdegree)
    if x_degree > 180:
        x_degree = x_degree - 360
    cos_x = 0
    x_radians = convert_degrees_to_radians(x_degree)
    for i in range(10):
        sign = (-1) ** i
        cos_x += sign * (x_radians ** (2 * i)) / jiecheng(2 * i)
    return round(cos_x, 10)

