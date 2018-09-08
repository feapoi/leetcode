class TwoSum(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # i is index
        maps = {}
        for i in range(len(nums)):
            if target - nums[i] in maps:
                return maps[target - nums[i]], i
            maps[nums[i]] = i
        return -1, -1
a = [1,11,22,3]
b = 33
two_sum = TwoSum()
c, d = two_sum.twoSum(a, b)
print(c, d)