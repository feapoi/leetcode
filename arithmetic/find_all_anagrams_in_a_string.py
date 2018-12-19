# problem：
#  找到s中包含p的位置，无视p的顺序
#  例     "cbaebabacd"  "abc"
#  结果   0 6
#
# solution
# 滑动窗口
import collections
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        count = []
        lenP = len(p)
        tem = {}
        temP = {}
        for j in p:
            if j in temP:
                temP[j] += 1
            else:
                temP[j] = 1
        for i in range(len(s)):
            if i < lenP:
                if s[i] in tem:
                    tem[s[i]] += 1
                else:
                    tem[s[i]] = 1
                if temP == tem:
                    count.append(0)
            else:
                if s[i] in tem:
                    tem[s[i]] += 1
                else:
                    tem[s[i]] = 1
                tem[s[i - lenP]] -= 1
                if tem[s[i - lenP]] == 0:
                    tem.pop(s[i - lenP])
                if temP == tem:
                    count.append(i - lenP + 1)
        return count

print(Solution().findAnagrams("acdcaeccde","c"))