# problem：
#  给出一个数组，求里面最小一段连续的数的长度，把这段排序之后，数组就会有序
#  需要注意的情况：
#    1.目标数组前后会有相同的数字
#    2.不能把出现倒序的地方作为起始点，因为倒序的点可能比前面几个数都要小
#      实在要这么做，要重新遍历一次，如方法3，这样做可以节省了方法2的栈空间
# solution
#   1.排序比较，对不上的序列就是需要排序序列
#   2.栈遍历找出起始点和结束点
#   3.
class Solution:
    def findUnsortedSubarray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1 = sorted(nums)
        numsLen = len(nums)
        start = numsLen
        end = 0
        for i in range(numsLen):
            if nums[i] != nums1[i]:
                start = min(start, i)
                end = max(end, i)
        print(end, start)
        return max(end - start + 1, 0)

    def findUnsortedSubarray2(self, nums):
        stack = []
        lenNum = len(nums)
        l = lenNum
        r = 0
        for i in range(lenNum):
            while stack and nums[stack[-1]] > nums[i]: ## 会和所有前面的数作比较，且解决了重复的问题
                l = min(l, stack.pop())
            stack.append(i)
        stack = []
        for i in reversed(range(lenNum)):
            while stack and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)
        if r - l > 0:
            return r - l + 1
        else:
            return 0

    def findUnsortedSubarray3(self, nums):
        minNum = float('inf')
        maxNum = float('-inf')
        flag = False
        lenNum = len(nums)
        for i in range(1, lenNum):
            if nums[i] < nums[i - 1]:
                flag = True
            if flag:
                minNum = min(minNum, nums[i])
        flag = False
        for i in reversed(range(lenNum - 1)):
            if nums[i] > nums[i + 1]:
                flag = True
            if flag:
                maxNum = max(maxNum, nums[i])
        l,r = 0,0
        # 解决重复的问题
        for i in range(lenNum):
            if (minNum < nums[i]):
                l = i
                break
        for i in reversed(range(lenNum)):
            if (maxNum > nums[i]):
                r = i
                break
        if r - l > 0:
            return r - l + 1
        else:
            return 0


print(Solution().findUnsortedSubarray3([2,6,4,8,10,9,15]))