class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        n = len(nums) // 2
        pos = len(nums) // 2
        while n > 0:
            nums.insert(pos, nums.pop(0))
            n -= 1
            pos += 1
        return nums

s = Solution()
print(s.wiggleSort([3,4,5,2,3,2,1]))