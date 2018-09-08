class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        key = 1
        value = "1"
        while key < n:
            fk = 0
            fv = 0
            result = ""
            for i in range(len(value)):
                if i == 0:
                    fk = 1
                    fv = value[i]
                elif value[i] != value[i - 1]:
                    result += str(fk)
                    result += fv
                    fk = 1
                    fv = value[i]
                else:
                    fk += 1
            result += str(fk)
            result += fv
            key += 1
            value = result
        return value
s = Solution()
print(s.countAndSay(5))
