# 四则运算
class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        num = 0
        sign = "+"  # 第一个数相当于是加
        for i, c in enumerate(s):
            if c.isdigit():                     ## 多位数字的处理方式
                num = 10 * num + int(c)

            # 当遇到一个新的运算符时，再去算前面的运算符和数，
            # 最后一个数例外
            if c in ["+", "-", "*", "/"] or i == len(s) - 1:
                # 按先乘除后加减的规则
                # 加减直接入栈
                # 乘除pop出上一个数，计算完再放回
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    val = stack.pop()
                    stack.append(val * num)
                elif sign == "/":
                    val = stack.pop()
                    stack.append(int(val / num))

                num = 0  # 每次计算完num归零，num是用来处理多位数
                sign = c # 因为每个运算符号都是处理下一个数

        return sum(stack)

s = Solution()
print(s.calculate("3333+2*2"))