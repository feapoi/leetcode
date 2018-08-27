class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)

s = Solution()
print(s.searchInsert([1,3,5,6], 7))