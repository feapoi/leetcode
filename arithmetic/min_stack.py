# problem：
#  实现push pop top getMin功能的栈
#
# solution
# 由于只要最小值，插入的时候多插入一个值来做最小值判断就可以了
# 比加一个变量记录最小值更方便
# pop的时候不需要考虑最小值变化
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.stack:
            self.stack.append(min(self.stack[-2], x))
        else:
            self.stack.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-2]