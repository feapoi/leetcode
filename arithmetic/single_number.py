# problem：
#  给定一个数组，里面的数都有两个，从中找出那一个只有一个的数
#  例     [1,1,2,2,3]
#  结果   3
#
# solution
# 1.位运算 异或

class Solution:
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        for i in nums:
            temp ^= i
        return temp

print(Solution().singleNumber1([1,2,3,1,2]))