# problem：
#  全排列
#  例     [1,2,3]
#  结果   [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]
#
# solution
# 递归 回溯
class Solution:
    def doSubsets(self, nums, now_list, now_num, res):
        res.append(now_list.copy())
        for i in range(now_num, len(nums)):
            now_list.append(nums[i])
            self.doSubsets(nums, now_list, i + 1, res)
            now_list.pop()    ##把这一层加的数去掉

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.doSubsets(nums, [], 0, res)
        return res


print(Solution().subsets("abc"))