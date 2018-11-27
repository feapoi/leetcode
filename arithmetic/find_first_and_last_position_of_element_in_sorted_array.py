# problem：
# 给出一个乱序列表，一个目标值，求出目标值首次出现和最后一次出现的index
#  例 [5,7,7,8,8,10]  8
#  结果 [3,4]
#
# solution:
# 线性扫描，先从左扫描到第一个，再从右开始扫描

class Solution:
    def searchRangeLinearScan(self, nums, target):
        nums_len = len(nums)
        str, end = -1,-1
        for i in range(len(nums)):
            if target == nums[i]:
                str = i
                for j in range(nums_len - i):
                    if target == nums[nums_len - j - 1]:
                        end = nums_len - j - 1
                        break
                if end == -1:
                    end = str
                return [str, end]
        return [str, end]

s = Solution()
b = s.searchRangeLinearScan([5,7,7,8,8,10], 1)
print(b)