# calculator_logic.py

# 导入三角函数的计算方法
from sin_taylor import sin_taylor
from cos_taylor import cos_taylor
from arcsin_taylor import arcsin_taylor
from arctan_newton import arctan_newton
import re

# 计算器逻辑类
class CalculatorLogic:
    # 移除最后一个字符的方法
    def remove_last_character(self, text):
        if text == '':
            return ''
        if text[-1] == '(' and len(text) >= 5 and text[-5] not in self.num_and_op:
            return text[:-5]
        elif text[-1] == '(' and text[-2] not in self.num_and_op:
            return text[:-4]
        else:
            return text[:-1]

    # 计算表达式的方法
    def calculate(self, expression):
        return self._evaluate_expression(expression)

    # 私有方法：评估表达式
    def _evaluate_expression(self, expression):
        if expression.isdigit():  # 如果表达式只包含一个数字，则直接返回该数字
            return float(expression)
        else:
            # 处理三角函数
            expression = self._handle_trigonometric_functions(expression)
            # TODO: 处理未完成的四则运算
            # 处理运算符
            return self._handle_operator(expression)

    # 私有方法：处理三角函数
    def _handle_trigonometric_functions(self, expression):
        trig_functions = ['sin', 'cos', 'asin', 'atan']
        # print("Inside _handle_trigonometric_functions")
        for func in trig_functions:
            while True:
                match = re.search(r'\b' + re.escape(func) + r'\b', expression)
                if match:
                    index = match.start()
                    opening_bracket_index = expression.find('(', index)
                    closing_bracket_index = self._find_closing_bracket(expression, opening_bracket_index)
                    if closing_bracket_index != -1:
                        angle_expr = expression[opening_bracket_index + 1: closing_bracket_index]
                        angle_value = self._evaluate_expression(angle_expr)
                        if func == 'sin':
                            result = sin_taylor(angle_value)
                        elif func == 'cos':
                            result = cos_taylor(angle_value)
                        elif func == 'asin':
                            if -1 <= angle_value <= 1:
                                result = arcsin_taylor(angle_value)
                            else:
                                raise ValueError("Input out of range [-1, 1] for asin")
                        elif func == 'atan':
                            result = arctan_newton(angle_value)
                        expression = expression.replace(expression[index: closing_bracket_index + 1], str(result))
                    else:
                        break
                else:
                    break
        return expression

    # 私有方法：找到闭合括号
    def _find_closing_bracket(self, expression, opening_index):
        count = 1
        for i in range(opening_index + 1, len(expression)):
            if expression[i] == '(':
                count += 1
            elif expression[i] == ')':
                count -= 1
                if count == 0:
                    return i
        return -1

    # 私有方法：处理运算符
    def _handle_operator(self, expression):
        operators = ['+', '-', '*', '/', '^']  # 支持的运算符列表

        for operator in operators:
            # 找到当前表达式中的第一个运算符
            index = expression.find(operator)
            if index != -1:
                left_operand = self._evaluate_expression(expression[:index].strip())
                right_operand = self._evaluate_expression(expression[index + 1:].strip())
                operator_func = self._get_operator_function(operator)
                return operator_func(left_operand, right_operand)

        # 如果没有运算符，则直接返回表达式的值
        return float(expression)

    # 私有方法：获取运算符函数
    def _get_operator_function(self, operator):
        if operator == '+':
            return lambda x, y: x + y
        elif operator == '-':
            return lambda x, y: x - y
        elif operator == '*':
            return lambda x, y: x * y
        elif operator == '/':
            return lambda x, y: x / y
        elif operator == '^':
            return lambda x, y: x ** y
