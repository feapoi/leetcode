# problem：
# 给出一个没有重复元素列表 和 一个目标值，问列表中的元素相加等于目标值的所有组合，一个元素可以使用多次
#  例 [1,2,3] 4
#  结果 [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2]]
#
# solution:
# 1.dfs(Depth First Search)优先深度算法
#   

class Solution:
    def combinationSum(self, nums, target):
        res = []
        nums.sort()
        def dfs(left, path, idx):
            if not left: res.append(path[:])
            else:
                for i, val in enumerate(nums[idx:]):
                    if val > left: break
                    dfs(left - val, path + [val], idx + i)      ##  idx + i
        dfs(target, [], 0)                                      ##  idx代表之前遍历的个数     i代表当前轮遍历的个数
        return res

s = Solution()
print(s.combinationSum([1,2,3], 4))