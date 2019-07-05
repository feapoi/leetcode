# problem：
#  把一个字符串转换为数字
#  要求：必须首位为正负符号或者数字，忽视空格
#
#  例：   4193 with words
#  结果： 4193
#
# solution
# 正则表达式
import re
class Solution:
    # @return an integer
    def myAtoi(self, str):
        str = str.strip()
        str = re.findall('^[\+\-0]*\d+', str)
        try:
            result = int(''.join(str))
            max = 2147483647
            min = -2147483648
            if result > max:
                return max
            elif result < min:
                return min
            else:
                return result
        except:
            return 0

print(Solution().myAtoi("   111"))