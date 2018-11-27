# problem：
# 给出一个列表表示墙的高度，求最大积水的体积
#  例 [0,1,0,2,1,0,1,3,2,1,2,1]
#  结果 6
#
# solution:
# 先从做往右，算出每个位置的最大积水等级（即左边的长度），一边的长度能决定最大积水体积
# 再从右往左，根据右边的最大长度，求出实际的积水体积
class Solution:
    def trap(self, height):
        waterLevel = []
        left = 0
        for h in height:
            left = max(left, h)
            waterLevel += [left]  # 填满到左最大高度
        print(waterLevel)
        right = 0
        for i, h in reversed(list(enumerate(height))):
            right = max(right, h)   ##墙从右往左遍历，最长长度
            waterLevel[i] = min(waterLevel[i], right) - h  # min（该位置左边墙最大长度，右边墙最大长度 ） - 该位置长度
        print(waterLevel)                                  # == 最大积水值
        return sum(waterLevel)

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

