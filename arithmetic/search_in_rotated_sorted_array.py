# problem：
# 一个升序的数组可能围绕某个点旋转，没有重复的数据，求目标值的index
#  例 [5,6,7,8,1,2,3,4]   2
#  结果 5
#
# solution:
# 通过确定值在那一边，用二分法处理
#
class Solution:
    def search(self, nums, target):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            ## target都在多的那一边，过了中点
            ## 例[7,8,9,1,2,3,4,5] 里的 1,2,3,4,5
            if (nums[mid] < nums[0]) == (target < nums[0]):
                if (nums[mid] < target):    ## [7,8,9,1,2,3,4,5]   4
                    lo = mid + 1
                elif (nums[mid] > target):  ## [5,6,7,8,9,1,2]   6
                    hi = mid
                else:                       ## nums[mid] == target
                    return mid
            elif target < nums[0]:          ## [5,6,7,8,9,1,2]   2
                lo = mid + 1
            else:
                hi = mid                    ## [7,8,9,1,2,3,4,5]   8

        return -1

s = Solution()
print(s.search([5,6,1,2,3,4,5], 1))