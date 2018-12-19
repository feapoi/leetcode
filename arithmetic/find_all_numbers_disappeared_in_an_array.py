# problem：
#  一个乱序数组中，按顺序由1递增，有的数有两个，有的数没有，求空缺的数
#  例     [4,3,2,7,8,2,3,1]
#  结果   [5,6]
#
# solution
# 先遍历nums,把数字对应位置的数翻转，不能翻转两次
# 这样剩余的数就是空缺的数
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in nums:
            # neat. using negative to preserve value
            j = abs(i) - 1
            if nums[j] >= 0:
                nums[j] = -nums[j]

        return [i + 1 for i, num in enumerate(nums) if num > 0]