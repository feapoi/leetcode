# problem：
#  给定一个二叉树，判断二叉树是不是镜像的
#  例     [1,2,2,3,4,4,3]       [1,2,2,null,3,null,3]
#  结果   true                  false
#
# solution
# 广搜BFS

import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        left_deque = collections.deque()
        right_deque = collections.deque()
        left_deque.append(root.left)
        right_deque.append(root.right)
        while(left_deque and right_deque):
            this_left = left_deque.popleft()
            this_right = right_deque.popleft()
            if (not this_left and not this_right):
                continue
            elif (this_left is None) != (this_right is None):
                return False
            if this_left.val != this_right.val:
                return False
            left_deque.append(this_left.left)
            left_deque.append(this_left.right)
            right_deque.append(this_right.right)
            right_deque.append(this_right.left)
        return True


