# problem：
# 一个列表中，取三个数，相加为0，列出所有的情况
#  例 [-1, 0, 1, 2, -1, -4]
#  结果 [[-1, 0, 1],[-1, -1, 2]]
#
# solution:
# 一个值遍历整个表，然后其他两个值赋值为第一个值后面一个值，和最后一个值
# 其他两个值不断靠近，直到相等，第一个值循环到下一个数
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()         ##先排序
        numslen = len(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:continue
            l = i + 1
            r = numslen - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while l < r and nums[r] == nums[r+1] : r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return result

s =Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))