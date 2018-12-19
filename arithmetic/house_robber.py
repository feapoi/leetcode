# problem：
#  给出一个数组，从任意点开始前进，每次前进步数大于1，求经过的点的值累加最大是多少
#  例     [2,7,9,3,1]
#  结果   12
#
# solution
# 1.使用动态规划
#   f(0) = nums[0]
#   f(1) = max(nums[0], nums[1])
#   f(k) = max(f(k - 2) + nums[k], f(k - 1))
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = 0
        now = 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now