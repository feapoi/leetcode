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