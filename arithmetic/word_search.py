# problem：
#  字符搜索，在一个字符二维数组中，是否能找到连续的某个字符串
# 例：[
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# "ABCCED"
#  结果   True
#
# solution
# DFS(深度优先搜索)

class Solution:
    def exist(self, board, word):
        visit = set()
        self.is_found = False
        c_word = ""
        path = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        len1 = len(board)
        len2 = len(board[0])
        def backtrack(c_word, l, r):
            c_word += board[l][r]
            visit.add((l,r))
            if c_word == word:
                self.is_found = True
                return
            for dx,dy in path:
                if ((l + dx, r + dy) not in visit
                    and 0 <= l + dx < len1
                    and 0 <= r + dy < len2
                    and word.startswith(c_word)
                    and self.is_found == False):
                        backtrack(c_word, l + dx, r + dy)
            visit.remove((l,r))
        for i in range(len1):
            for j in range(len2):
                if self.is_found == False:
                    backtrack(c_word, i, j)
        return self.is_found

print(Solution().exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "BBB"))