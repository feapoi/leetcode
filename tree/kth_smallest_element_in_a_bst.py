# Definition for a binary tree node.
# 找出二叉搜索树中的第k小的数
# 思路：找出第n小的节点，也就是找到一个节点，该节点左边有k - 1个节点
#       先从头节点，一路到最左节点，把经过的节点都放到list中
#       然后再一路往上走，每走一个节点，k - 1，直到k为0为止
#       注意：经过的节点都要尽量去走右节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        return root.val

