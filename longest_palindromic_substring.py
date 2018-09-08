class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_s = ""
        if len(s) == 1:
            return s[0]
        for i in range(len(s)):
            s1 = self.getThisLong(s, i ,i + 1)
            if len(s1) >= len(max_s):
                max_s = s1
            s2 = self.getThisLong(s, i ,i + 2)
            if len(s2) >= len(max_s):
                max_s = s2
        return max_s

    def getThisLong(self, s, start, end):
        while(start >= 0 and end < len(s) and s[start] == s[end]):
            start = start - 1
            end = end + 1
        return s[start + 1 : end]

s = Solution()
print(s.longestPalindrome("abcdre"))