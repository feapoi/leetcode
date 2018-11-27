# problem：
#  无重复元素的全排列
#  例 [1,2,3]
#  结果 [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# solution:
# dfs(优先深度搜索) 回溯
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result_list = []
        def permuteHelper(res, current, rem):
            # Base case: No remaining element
            if not rem:
                res.append(current)

            # Recursive case
            for i in range(len(rem)):
                permuteHelper(res, current + [rem[i]], rem[:i] + rem[i + 1:])

        permuteHelper(result_list, [], nums)
        return result_list
