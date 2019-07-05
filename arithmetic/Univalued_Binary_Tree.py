# 判断树里的所有节点是否相等
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        elif root.left and root.right:
            return root.left.val == root.val and root.right.val == root.val and self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        elif root.left:
            return root.left.val == root.val and self.isUnivalTree(root.left)
        elif root.right:
            return root.right.val == root.val and self.isUnivalTree(root.right)
        else:
            return True