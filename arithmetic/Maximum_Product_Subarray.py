# 乘积最大的子数组
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        record=[nums[0],nums[0]]
        res=nums[0]
        for v in nums[1:]:
            # 把当前数， 当前数乘原来的最大最小值
            # （以为符号，负号最小再乘以负号就是最大，所以最大最小值都要保存）
            record=[max(v,v*record[0],v*record[1]),min(v,v*record[0],v*record[1])]
            # 和之前的最大值进行比较
            res=max(res,record[0])
        return res

s = Solution()
print(s.maxProduct([1, 4, 0, 2, 3]))