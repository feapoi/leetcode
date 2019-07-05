# 两个字符串是否是字母相同异序词
from collections import Counter
class Solution:
    def isAnagram_1(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)
        return s_count == t_count
    def isAnagram_2(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        for j in t:
            if j in t_dict:
                t_dict[j] += 1
            else:
                t_dict[j] = 1
        return s_dict == t_dict
print(Solution().isAnagram_2("abf", "fba"))