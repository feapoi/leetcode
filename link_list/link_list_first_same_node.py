# 两个链表找到第一个相同的节点
# 只要第一个节点相同，后面的节点肯定都是相同的
# 先求出两条链表的长度，然后让长的链表先走 lenA - LenB步
# 然后两个条链表同步next，判断节点是否相同
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def create(self, n, m):
        t = ListNode(999)
        nList = ListNode(n[0])
        nList1 = nList
        for i in range(1, len(n)):
            nList.next = ListNode(n[i])
            nList = nList.next
        nList.next = t

        mList = ListNode(m[0])
        mList1 = mList
        for i in range(1, len(n)):
            mList.next = ListNode(m[i])
            mList = mList.next
        mList.next = t

        return nList1,mList1

    def show(self, l):
        while l.next:
            print(l.val)
            l = l.next
        print(l.val)

    def linkListFirstSameNode(self, root1, root2):
        len1 = getLinkListLen(root1)
        len2 = getLinkListLen(root2)
        if len1 > len2:
            for i in range(len1 - len2):
                root1 = root1.next
        else:
            for i in range(len2 - len1):
                root2 = root2.next
        while root1:
            if root1 == root2:
                return root1.val
            root1 = root1.next
            root2 = root2.next
        return False

def getLinkListLen(root):
    len = 1
    while root.next:
        root = root.next
        len += 1
    return len

s = Solution()
l1, l2 = s.create([1,2,3], [3,4,5])
print(s.linkListFirstSameNode(l1, l2))