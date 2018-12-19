# problem：
#  给定一组未排序的区间，要求把重叠的区间合并
#  例     [[1,3],[2,6],[8,10],[15,18]]
#  结果   [[1,6],[8,10],[15,18]]
#
# solution
# 先用区间开始的点排序
# for循环对比本区间的末尾，和下一个区间的开始即可知是否可以合并
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # lambda 这里的作用是取出Interval结构中的start
        res = []
        intervals.sort(key = lambda x:x.start)
        for interval in intervals:
            if res == [] or res[-1].end < interval.start:
                res.append(interval)
            else:
                res[-1].end = max(interval.end, res[-1].end)
        return res

res = Solution().merge([Interval(1,3),Interval(2,6)])
print(res)