class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
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