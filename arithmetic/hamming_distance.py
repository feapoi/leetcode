# problem：
#  hamming(汉明) distance, 求两个数的二进制位有多少不相同
#  例     1001   1100
#  结果   2

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        v = x ^ y                #对两个数取异，不同的位为1
        count = 0
        while v >= 1:           #取出所有的位数
            if v%2:             #如果最后一位不是0
                count += 1
            v //= 2
        return count
print(Solution().hammingDistance(3, 1))