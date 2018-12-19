# problem：
#  在不利用额外列表的情况下，把一个列表里的0都移动到最后去
#  例     [0,1,0,2,3]
#  结果   [1,2,3,0,0]
#
# solution
# 把0的序列逐渐推进，记录0序列最后的坐标
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        last_zero = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                if last_zero == -1:
                    last_zero = i
            else:
                if last_zero != -1:
                    nums[last_zero],nums[i] = nums[i],nums[last_zero]
                    last_zero += 1