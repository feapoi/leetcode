# problem：
#  两个字符串A B ，问B中有多少字符也在A中
#  例     “AB” “ABCAB”
#  结果   4

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for i in S:
            if i in J:
                count += 1
        return count