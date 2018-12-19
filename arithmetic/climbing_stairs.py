# problem：
#  爬楼梯，可以爬一步或者两步，求有多少种方法
#  例     3
#  结果   3
#
# solution
# 1.使用动态规划
#   看出来每一层的方法数等于前两层相加，正好符合斐波那契数列

import math
class Solution:
    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]

    def climbStairs2(self, n):
        sqrt5=math.sqrt(5)
        fibn=math.pow((1+sqrt5)/2,n+1)-math.pow((1-sqrt5)/2,n+1)
        return int(fibn/sqrt5)

print(Solution().climbStairs2(2))