class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        kv = {"]":"[", ")":"(", "}":"{"}
        temporary = []
        for i in s:
            if i in kv.values():
                temporary.append(i)
            elif i in kv.keys():
                if temporary == [] or kv[i] != temporary.pop():
                    return False
            else:
                return False
        return temporary == []
s = Solution()
print(s.isValid("["))