# problem：
#  返回一个数组，i位置的值为nums中除了i的其他数的乘积
#  例     [1,2,3,4,5], [1,2,0,4,5]
#  结果   [120, 60, 40, 30, 24] ,[0, 0, 40, 0, 0]
#
# solution
# 先从右往左累乘，在从左往右累乘

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len1 = len(nums)
        tempNums = [1] * len1
        for i in range(len1 - 2, -1, -1):
            tempNums[i] = tempNums[i + 1] * nums[i + 1]
        temp = 1
        for i in range(len1):
            nums[i] ,temp= tempNums[i] * temp, temp * nums[i]
        return nums

print(Solution().productExceptSelf([1,2,3,4,5]))