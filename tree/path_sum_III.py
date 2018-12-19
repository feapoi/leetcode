# problem：
#  判断一个二叉树中，存在几段连续的数，相加值为指定值，不一定要从root开始
#
# solution
# 1.Brute force 有很多重复遍历 O(n^2)
# 2.带记忆功能的优化        O(n)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution1:
    def __init__(self):
        self.count = 0        ##只能定义在上面，不然递归每次都会初始化
    def pathSum1(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def pathSumHelper(point, su):
            if not point:
                return
            if su + point.val == sum:
                self.count += 1
            if point.left:
                pathSumHelper(point.left, su + point.val)
            if point.right:
                pathSumHelper(point.right, su + point.val)

        if not root: return 0

        pathSumHelper(root, 0)
        if root.left:
            self.pathSum1(root.left, sum)
        if root.right:
            self.pathSum1(root.right, sum)
        return self.count


class Solution2(object):
    def pathSum2(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def dfs(root, total, sum):
            if not root:
                return
            nowTotal = total + root.val
            if nowTotal - sum in memory:
                self.count += memory[nowTotal - sum]
            if nowTotal in memory:
                memory[nowTotal] += 1
            else:
                memory[nowTotal] = 1
            dfs(root.left, nowTotal, sum)
            dfs(root.right, nowTotal, sum)
            memory[nowTotal - sum] -= 1
        self.count = 0
        memory = {0:1}
        dfs(root, 0, sum)
        return self.count
