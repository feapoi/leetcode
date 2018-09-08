class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        for i in range(len(nums)):
            if i != 0:
                if nums[i] != nums[i-1]:
                    nums[index] = nums[i]
                    index += 1
            else:
                index += 1
        return index

s = Solution()
print(s.removeDuplicates([1,1,2]))
