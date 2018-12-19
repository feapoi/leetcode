# problem：
#  两个二叉树合并，有节点相加，单节点代替
#
# solution
# 递归
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees1(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees1(t1.left, t2.left)
        t1.right = self.mergeTrees1(t1.right, t2.right)
        return t1

