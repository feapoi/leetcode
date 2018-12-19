# problem：
#  找出数组中大于半数的元素，不考虑空和不存在的情况
#  例     [1,1,1,2,2]
#  结果   1
#
# solution
# 1.python自带Counter结构

import collections
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len1 = (len(nums) // 2) + 1
        counter = collections.Counter(nums)
        for i in counter:
            if counter[i] >= len1:
                return i

print(Solution().majorityElement([1,1,2,2,2]))
