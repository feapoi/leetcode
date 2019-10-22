## 不用loop循环判断n是否是3次幂
## 3的n次方 个位是在 3 9 7 1 四个数循环的

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last = str(n)[-1]
        power = None

        if last == '1':
            power = 0
        elif last == '3':
            power = 1
        elif last == '9':
            power = 2
        elif last == '7':
            power = 3

        if power != None:
            while 3 ** power < n:
                power += 4

            if 3 ** power == n:
                return True

        return False

s = Solution()
print(s.isPowerOfThree(27))