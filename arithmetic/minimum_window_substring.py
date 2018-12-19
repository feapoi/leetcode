# problem：
#  给出两个字符串A,B，求A中包含B中所有字符的最小连续片段
#  例     ADOBECODEBANC， ABC
#  结果   BANC
#
# solution
# 移动窗口

import collections
class Solution():
    # 原始版
    def minWindow1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        dict_t = collections.Counter(t)
        # 短字符串的种类数量
        required = len(dict_t)
        l, r = 0, 0
        # 多少种字符已经完成收集
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None
        while r < len(s):
            character = s[r]
            # 右边取一个数放入到窗口中
            window_counts[character] = window_counts.get(character, 0) + 1
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            # 窗口中的值已经满足条件
            while l <= r and formed == required:
                # 去掉左边那个值
                character = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                window_counts[character] -= 1
                # 此时要是不满足条件， 收集完成的数量 -1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

    # 优化版
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        dict_t = collections.Counter(t)
        required = len(dict_t)
        filtered_s = []
        for i, char in enumerate(s):
            # 只判断t里面存在的字符
            if char in dict_t:
                filtered_s.append((i, char))
        print(filtered_s)
        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None
        while r < len(filtered_s):
            character = filtered_s[r][1]
            window_counts[character] = window_counts.get(character, 0) + 1
            if window_counts[character] == dict_t[character]:
                formed += 1
            # 缩减窗口
            while l <= r and formed == required:
                character = filtered_s[l][1]
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)
                window_counts[character] -= 1
                if window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

print(Solution().minWindow("ADOBECODEBANC", "ABC"))