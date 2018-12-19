# problem：
#  给定一个m * n地图，机器人在1,1，走过某点则加上某点，求走到m,n 数值最小的路径
#  例     [
#           [1,3,1],
#           [1,5,1],
#           [4,2,1]
#         ]
#  结果   7
#
# solution
# 1.使用动态规划
#   因为到达i,j 点最后必然经过两点 i-1,j 和 i,j-1
#   所以可以看做到达这两个点的情况
#   总结规律DP[i,j] += min (DP[i-1,j] + DP[i,j-1])
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[m - 1][n - 1]

print(Solution().minPathSum(
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]))