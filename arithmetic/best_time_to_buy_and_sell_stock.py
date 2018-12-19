# problem：
#  给定一个数组，表示股价变化，求以最优方式买入和卖出，能有多少收益
#  例     [7,1,5,3,6,4]
#  结果   5
#
# solution
# DP 动态规划
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        distance = [0]
        for i in range(1, len(prices)):
            distance.append(max(0, prices[i] - prices[i - 1]) + distance[i - 1])
        return max(distance)

print(Solution().maxProfit([1,2,3]))