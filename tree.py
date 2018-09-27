# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        rootval = pre[0]
        print(rootval)
        p = self.find(pre[0], tin)
        if p != None:
            root.left = self.reConstructBinaryTree(pre[1:p + 1], tin[:p])
            root.right = self.reConstructBinaryTree(pre[p + 1:], tin[p + 1:])
        return root

    def find(self, val, tin):
        for j in range(len(tin)):
            if tin[j] == val:
                return j
        return None

s = Solution()
r = s.reConstructBinaryTree([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])
print(r.val)