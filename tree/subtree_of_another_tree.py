# problem：
#  判断一个树t是不是另一个树s的子树，必须是到最后的子节点，在中间不算
#
# notice:
#  开始错误的认为s每个子节点的深度是相同的，这样算出两个树的深度差，就可以只用比较头结点是那个深度的子树
#
class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # 给出两个头节点，比较两个树
        def equals(s2, t2):
            # 一步一步往下判断
            if (s2 == None and t2 == None):
                return True
            if (s2 == None or t2 == None):
                return False
            return s2.val == t2.val and equals(s2.left, t2.left) and equals(s2.right, t2.right)
        def traverse(s1, t1):
            # 对比的对象不为None，因为t不可能是None
            # 然后以当前节点为起点，来进行判断
            # 同时or子节点，也存在True的可能
            return s1 != None and (equals(s1, t1) or traverse(s1.left, t1) or traverse(s1.right, t1))
        return traverse(s,t)