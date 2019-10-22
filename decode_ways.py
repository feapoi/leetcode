class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 26
        self.res = 0
        def backtrack(q, w, num):
            if not q:
                self.res += 1
                return
            if w.last
        backtrack(s, [], 0)
