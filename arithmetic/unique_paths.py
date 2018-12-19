# problem：
#  给定一个m * n地图，机器人在1,1，求走到m,n 有多少条不同路径
#  例     m = 3, n = 2
#  结果   3
#
# solution
# 1.利用阶乘的组合公式 !(m + n) / !m * !n
# 2.使用动态规划
#   因为到达i,j 点最后必然经过两点 i-1,j 和 i,j-1
#   所以可以看做到达这两个点的情况
#   总结规律DP[i,j] = DP[i-1,j] + DP[i,j-1]
import math
class Solution:
    def uniquePaths1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        nT = m+n-2
        rT = m-1
        return int(math.factorial(nT)/(math.factorial(rT)*math.factorial(nT-rT)))

    def uniquePaths2(self, m, n):
        DP = [0] * m
        for i in range(0, m):
            DP[i] = [0] * n
        DP[0][0] = 1
        for j in range(1, m):
            DP[j][0] = 1
        for k in range(1, n):
            DP[0][k] = 1
        for p in range(1, m):
            for q in range(1, n):
                DP[p][q] = DP[p - 1][q] + DP[p][q - 1]
        return DP[m - 1][n - 1]

print(Solution().uniquePaths2(7,3))