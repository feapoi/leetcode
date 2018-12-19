# problem：
#  荷兰国旗划分问题，把3种散乱的数字分类排好
#  例     [2,0,2,1,1,0]
#  结果   [0,0,1,1,2,2]
#
# solution
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums) - 1
        ## 可以看做两个点向中间靠近
        while white <= blue:
            # 左序列 + 1，左坐标和中坐标右移一位
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            # 中序列 + 1，中坐标右移一位
            elif nums[white] == 1:
                white += 1
            # 右序列 + 1，右坐标左移一位
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
        return nums

print(Solution().sortColors([2,0,2,1,1,0]))