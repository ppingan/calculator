import math
import random
from cosx import cos

#取绝对值
def abs(n):
    if n>=0:
        return n
    else:
        return -n

#测试单个角度的计算值
def test_cos(x_degree):
    threshold = 0.0001
    #调用math包
    cos_result = round(math.cos(math.radians(x_degree)), 10)
    print("{}的基准值为{}".format(x_degree, cos_result))
    #使用泰勒展开
    cos_tylor = cos(x_degree)
    print("{}的泰勒展开计算值为{}".format(x_degree, cos_tylor))
    #计算偏差
    bias = cos_tylor - cos_result
    if abs(bias) <= threshold:
        tag = True
        print({"该角度计算正确，误差低于阈值"})
    else:
        tag = False
        print({"该角度计算不正确，误差高于阈值"})
    return tag

#测试自动化，随机产生多个随机数进行测试，只要一个误差超过阈值就判定函数不精确
def auto_test_cos(test_num):
    test_samples = random.sample(range(-1000, 1000), test_num)
    err_num = 0
    for test_sample in test_samples:
        tag = test_cos(test_sample)
        if not tag:
            err_num = err_num + 1
    if err_num == 0:
        print("################################################")
        print("测试{}个样本，所有样本都准确：函数正确".format(test_num))
    else:
        print("################################################")
        print("测试{}个样本，函数不精确，错误样本数为：{}".format(test_num, err_num))

test_num = 100
auto_test_cos(test_num)