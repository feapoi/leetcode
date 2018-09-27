class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        for i, num in enumerate(nums):
            if num < 0 or num > len(nums):
                nums[i] = 0

        print(nums)

        for i in range(len(nums)):
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
print(s.firstMissingPositive([2,1,6,4]))