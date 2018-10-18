class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        max = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack == []:
                    stack.append(i)
                else:
                    stack.pop()
                    if stack == []:
                        stack.append(i)
                    else:
                        if max < (i - stack[-1]):
                            max = (i - stack[-1])
        return max
s = Solution()
print(s.longestValidParentheses("()()()"))