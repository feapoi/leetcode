class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }
        high = 0
        result = 0
        for letter in s[::-1]:
            value = values[letter]
            if value >= high:
                high = value
                result += value
            else:
                result -= value
        return result

s = Solution()
print(s.romanToInt("MIIIII"))