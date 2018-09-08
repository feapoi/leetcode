class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        stack = []
        strs.sort(key=len)              ## 按长度排序
        lengthOfArray = len(strs)
        if lengthOfArray == 0:
            return ""
        elif lengthOfArray == 1:
            return strs[0]
        i = 0
        lengthOf1stString = len(strs[0])
        while i != lengthOf1stString:
            stack.append(strs[0][i])
            i += 1
        i = 1
        count = 0
        while i != lengthOfArray:            ##遍历strs
            z = 0
            while z != len(stack):
                if strs[i][z] == stack[z]:
                    count += 1
                    z += 1
                else:
                    stack = stack[:count]
                    break
            count = 0
            i += 1
        return ''.join(stack)


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))