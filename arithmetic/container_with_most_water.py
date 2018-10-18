# problem：
# 给定一个非负没有排序的列表，按数值大小画成柱状图，求两根柱子之间存储水的最大面积
#  例 [1,8,6,2,5,4,8,3,7]
#  结果 49    {8 -> 7}
#
# solution:
# 两个值不断靠近
# 每次数值小的一边靠近一位，直到两个值靠到一起

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        hlen = len(height) - 1
        hstart = 0
        hend = len(height) - 1
        hmax = min(height[0], height[hlen]) * hlen
        while hstart != hend:
            if height[hstart] < height[hend]:
                hstart += 1
                hlen -= 1
                hmax = max(min(height[hstart], height[hend]) * hlen, hmax)
            else:
                hend -= 1
                hlen -= 1
                hmax = max(min(height[hstart], height[hend]) * hlen, hmax)
        return hmax
s = Solution()
print(s.maxArea([5,3,1,2,4]))