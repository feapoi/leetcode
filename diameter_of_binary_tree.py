# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def getDeep(node):
            if not node:
                return 0
            l = getDeep(node.left)
            r = getDeep(node.right)
            res = max(self.res, l + r)
            return max(l, r)
