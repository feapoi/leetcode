class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = nums.sort()
        numslen = len(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:continue
            l = i + 1
            r = numslen - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    nums.append([nums[i], nums[l], nums[r]])
