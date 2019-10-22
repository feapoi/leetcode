## 从一个元素可相同的数组中，找出全排列
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        nums.sort()
        def backtrack(n, m):
            if not n:
                self.res.append(m)
                return
            for i in range(len(n)):
                if i == 0 or (n[i - 1] != n[i] and i > 0):
                    backtrack(n[:i] + n[i + 1:], m + [n[i]])
        backtrack(nums, [])
        return self.res

s = Solution()
print(s.permuteUnique([1,1,3]))
