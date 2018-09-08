class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = ""
        max_len = 0
        for i in range(len(s)):
            if len(result) == 0:
                result = s[i]
            else:
                if result.find(s[i]) == -1:
                    result += s[i]
                else:
                    if max_len < len(result):
                        max_len = len(result)
                        place = result.find(s[i]) + 1
                        result = result[place:] + s[i]
                    else:
                        place = result.find(s[i]) + 1
                        result = result[place:] + s[i]
        if max_len < len(result):
            print(result)
            return len(result)
        else:
            return max_len
a = Solution()
b = a.lengthOfLongestSubstring("abcabcbb")
print(b)