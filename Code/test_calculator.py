import random
from CalculatorLogic import CalculatorLogic
import unittest
import math
from sin_taylor import sin_taylor
from cos_taylor import cos_taylor
from arcsin_taylor import arcsin_taylor
from arctan_newton import arctan_newton


class TestCalculatorLogic(unittest.TestCase):
    def setUp(self):
        self.calculator_logic = CalculatorLogic()
        self.allowed_error = 1e-4  # 允许的误差范围

    def test_sin_taylor(self):
        module_error = 0
        for _ in range(10):
            angle = random.uniform(-360, 360)
            expected_result = math.sin(math.radians(angle))
            actual_result = sin_taylor(angle)
            error = abs(expected_result - actual_result)
            module_error += error

        avg_error = module_error / 10
        print("sin_taylor的平均误差:", avg_error)
        self.assertLess(avg_error, self.allowed_error, "sin_taylor 函数的平均误差超过了允许的范围")

    def test_cos_taylor(self):
        module_error = 0
        for _ in range(10):
            angle = random.uniform(-360, 360)
            expected_result = math.cos(math.radians(angle))
            actual_result = cos_taylor(angle)
            error = abs(expected_result - actual_result)
            module_error += error

        avg_error = module_error / 10
        print("cos_taylor的平均误差:", avg_error)
        self.assertLess(avg_error, self.allowed_error, "cos_taylor 函数的平均误差超过了允许的范围")

    def test_arcsin_taylor(self):
        module_error = 0
        for _ in range(10):
            x = random.uniform(-1, 1)
            expected_result = math.degrees(math.asin(x))
            actual_result = arcsin_taylor(x)
            error = abs(expected_result - actual_result)
            module_error += error

        avg_error = module_error / 10
        print("arcsin_taylor1的平均误差:", avg_error)
        self.assertLess(avg_error, self.allowed_error, "arcsin_taylor 函数的平均误差超过了允许的范围")

    def test_arctan_newton(self):
        module_error = 0
        for _ in range(10):
            x = random.uniform(-100, 100)
            expected_result = math.degrees(math.atan(x))
            actual_result = arctan_newton(x)
            error = abs(expected_result - actual_result)
            module_error += error

        avg_error = module_error / 10
        print("arctan_newton的平均误差:", avg_error)
        self.assertLess(avg_error, self.allowed_error, "arctan_newton 函数的平均误差超过了允许的范围")

    def test_operator_evaluation(self):
        # 生成随机数表达式，并计算结果
        for _ in range(10):
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            op = random.choice(['+', '-', '*', '/'])
            expression = f"{num1}{op}{num2}"
            result = eval(expression)  # 使用eval计算结果
            calculated_result = self.calculator_logic.calculate(expression)
            self.assertEqual(result, calculated_result)

    def test_cal(self):
        result = self.calculator_logic.calculate('sin(45)+cos(40)')
        self.assertAlmostEqual(result, 1.4731, delta=self.allowed_error)

        result = self.calculator_logic.calculate('asin(0.5)+atan(1)')
        self.assertAlmostEqual(result, 75)


if __name__ == '__main__':
    test = TestCalculatorLogic()
    test.test_sin_taylor()
    test.test_cos_taylor()
    test.test_arcsin_taylor()
    test.test_arctan_newton()
    test.test_operator_evaluation()
    unittest.main()

