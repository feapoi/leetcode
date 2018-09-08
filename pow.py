class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n > 0:
            return self.doMyPow(x, n)
        else:
            return self.doMyPow(1/x, -n)

    def doMyPow(self, x, n):
        result = x
        while n > 1:
            if result == result * x or result == -result * x:
                if n % 2 == 0:
                    return result * result
                else:
                    return result
            result *= x
            n -= 1
        return result

s = Solution()
print(s.myPow(2, 2))


