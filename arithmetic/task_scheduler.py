# problem：
#  给定一个字符串，给定一个值n,相同的字符间的距离不能小于n
#  例     tasks = ["A","A","A","B","B","B"], n = 2
#  结果   A -> B -> idle -> A -> B -> idle -> A -> B.   8
#
# solution
# 找出空白格的数量
# 空白格的数量 = n * (maxVal - 1)

import collections
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # 首先把所有字符串按字符出现次数排序
        charMap = collections.Counter()
        for i in tasks:
            charMap[i] += 1
        charMap = sorted(charMap.items(), key=lambda charMap:charMap[1])
        charLen = len(charMap)
        (maxKey, maxVal) = charMap[charLen - 1]
        # 先假设空白格都是满的
        # 因为最后一行没有空白格，以及最大Key占了第一列
        # 空白格的数量 = n * (maxVal - 1)
        maxVal -= 1
        res = n * maxVal
        # 得到实际空白格的数量
        for j in reversed(range(charLen - 1)):
            (thisKey, thisVal) = charMap[j]
            res -= min(thisVal, maxVal)
        if res > 0:
            return res + len(tasks)
        else:
            # 空白格全部为空
            return len(tasks)

print(Solution().leastInterval("aaaabbbbcccd", 4))