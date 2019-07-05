# N位数每个相邻位相差K，的全排列
import math
class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        resList = [0,1,2,3,4,5,6,7,8,9]
        return self.numsSameConsecDiff1(N - 1, K, resList, 0)

    def numsSameConsecDiff1(self, N, K, resList, Bit):
        if N == 0:
            return resList
        newResList = []
        for i in resList:
            last = i // math.pow(10, Bit)
            if K == 0:
                if last != 0:
                    newResList.append(int(i + last * math.pow(10, Bit + 1)))
            else:
                if last + K < 10:
                    newResList.append(int(i + (last + K) * math.pow(10, Bit + 1)))
                if last - K > 0 or (last - K == 0 and N != 1):
                    newResList.append(int(i + (last - K) * math.pow(10, Bit + 1)))
        return self.numsSameConsecDiff1(N - 1, K, newResList, Bit + 1)

s = Solution()
print(s.numsSameConsecDiff(2, 0))