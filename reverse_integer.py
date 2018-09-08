class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        start = abs(x)
        result = 0
        while start >= 1:
            result = result * 10 + start % 10
            start = int(start/10)
        if result >= -pow(2, 31) and result <= pow(2, 31) - 1:
            if x > 0:
                return result
            else:
                return -result
        else:
            return 0

s = Solution()
print(s.reverse(1534236469))