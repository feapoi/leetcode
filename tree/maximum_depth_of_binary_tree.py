# problem：
#  求二叉树的最大深度
# solution
# 广搜BFS
# 深搜DFS
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepthBFS(self, root):
        deep = 0
        if root is None:
            return deep
        check_list = [root]
        while(check_list):
            deep += 1
            cur_list = []
            for i in check_list:
                if i.left:
                    cur_list.append(i.left)
                if i.right:
                    cur_list.append(i.right)
            check_list = cur_list
        return deep
    def maxDepthDFS(self, root):
        deep = 0
        if root is None:
            return deep
        check_list = [[root, 0]]
        while(check_list):
            this_point = check_list.pop()
            if this_point[0].left:
                check_list.append([this_point[0].left, this_point[1] + 1])
            else:
                deep = max(deep, this_point[1] + 1)
            if this_point[0].right:
                check_list.append([this_point[0].right, this_point[1] + 1])
            else:
                deep = max(deep, this_point[1] + 1)
        return deep

