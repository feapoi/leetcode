# problem：
#   给定一个无序列表，求从1开始往下第一个缺少的数
#  例 [9,8,4,1]
#  结果 2
#
# solution:
# 1.先去除无关的数（小于0， 和大于列表长度的数）
# 2.然后对其他的数进行排序，把他们放到自己的位置上
# 3.从第一个数往后遍历，找出空缺的数

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        for i, num in enumerate(nums):      ## enumerate会遍历nums的数据，并按顺序编号，index从0开始
            if num < 0 or num > len(nums):  ## [11,22] =>   [(0,11),(1,22)]
                nums[i] = 0                  ## 如果小于0 或者大于长度 肯定不在完整的序列中，忽略全部变成0

        print(nums)
        for i in range(len(nums)):          ##对非0的数进行排序
            ## 筛选条件 不等于0 没有排好序
            while (nums[i] != 0) and (nums[i] != i + 1) and (nums[i] != nums[nums[i] - 1]):
                tmp = nums[i]
                nums[i] = nums[tmp - 1]
                nums[tmp - 1] = tmp

        print(nums)
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1

        return len(nums) + 1

s = Solution()
print(s.firstMissingPositive([9,8,4,2]))