class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            x_str = str(x)
            flag = True
            while(x_str != ""):
                if x_str[0] == x_str[-1]:
                    print(x_str[0], x_str[-1])
                    x_str = x_str[1:-1]
                else:
                    flag = False
                    x_str = x_str[1:-1]
            return flag

s = Solution()
print(s.isPalindrome(122))
