# problem：
#  判断字符串中的回文数量
#
# solution:
# 可以看做包含多个大回文
# 大回文中的小回文可以通过小回文 和 大回文 中点的位置求出
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def manachers(S):
            A = '@#' + '#'.join(S) + '#$'
            Z = [0] * len(A)
            center = right = 0
            for i in range(1, len(A) - 1):    ## 排除了前面加的@ 和 $
                if i < right:                 ##因为一个大回文里，会有很多小回文
                    Z[i] = min(right - i, Z[2 * center - i])
                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:    ##确定该回文的半径
                    Z[i] += 1
                if i + Z[i] > right:
                    center, right = i, i + Z[i]
            return Z

        return sum((v+1)//2 for v in manachers(s))

s = Solution()
print(s.countSubstrings("aaa"))