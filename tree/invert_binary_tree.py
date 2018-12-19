# problem：
#  翻转整个树
#
# solution
# BFS
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        tree_stack = collections.deque()
        tree_stack.append(root)
        while tree_stack:
            t = tree_stack.pop()
            if t:
                t.left, t.right = t.right, t.left
                tree_stack.appendleft(t.right)
                tree_stack.appendleft(t.left)
        return root