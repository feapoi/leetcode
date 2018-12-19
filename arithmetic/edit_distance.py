# problem：
#  求把一个字符串变成另一个字符串需要多少步骤
#   可用步骤：
#       1.增加
#       2.删除
#       3.替换
#  例     "intention"       "execution"
#  结果   5
#         intention -> inention (remove 't')
#         inention -> enention (replace 'i' with 'e')
#         enention -> exention (replace 'n' with 'x')
#         exention -> exection (replace 'n' with 'c')
#         exection -> execution (insert 'u')
#
#
# solution
# 动态规划找出规律


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        if m * n == 0:
            return m + n
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] - 1)
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[m][n]
print(Solution().minDistance("intention", "execution"))