# problem：
#  给定一个数组，数组的值表示最多能前进的格数，判断从0开始走能不能走到终点
#  例     [2,3,1,1,4]       [3,2,1,0,4]
#  结果   true              false
#
# solution
# 可以看做一段段道路相互重叠，只需判断中间有没有断层
# 1.从左往右的动态规划 O(n^2)  O(n)
#    回溯的优化版，记录判断过的点，空间换时间，优点是能方便的获取全部路径
# 2.从右往左的动态规划 O(n^2)  O(n)
#    两个for循环
# 3.贪心算法 (Greedy) O(n)  O(1)
#    时间最短，而且不用额外的堆栈操作，缺点是不能获得路径
class Solution:
    def doCanJump1(self, position, nums, memo):
        len1 = len(nums)
        # 当回溯到判断过得点，直接返回结果
        if memo[position] != "U":
            return memo[position] == "G"
        maxjump = min(nums[position] + position, len1 - 1)
        # 得到能往后走的可能的点,排除本身的点
        for i in range(position + 1, maxjump + 1):
            if self.doCanJump1(i, nums, memo):
                memo[position] = "G"
                return True
        memo[position] = "B"
        # 走不了一步，直接返回false
        return False
    def canJump1(self, nums):
        len1 = len(nums)
        memo = []
        for i in range(len1):
            if i == len1 - 1:
                memo.append("G")
            else:
                memo.append("U")
        return self.doCanJump1(0, nums, memo)




    def canJump3(self, nums):
        len1 = len(nums)
        flag = len1 - 1
        for i in reversed(range(len1 - 1)):
            if i + nums[i] >= flag:
                flag = i
        return flag == 0

    # 与上面的相似，少一个列表反序操作
    def canJump4(self, nums):
        reach = 0
        for i in range(len(nums)):
            if reach >= i and i+nums[i] > reach: reach = i+nums[i]
        return reach >= len(nums)-1

s = Solution()
res = s.canJump1([3,2,1,0,4])
print(res)