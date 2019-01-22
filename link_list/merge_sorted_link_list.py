# 合并两个有序链表
class LinkNone:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def create(self, n):
        l = LinkNone(0)
        m = l
        for i in n:
            m.next = LinkNone(i)
            m = m.next
        return l

    def show(self, n):
        res = []
        n = n.next
        while n:
            res.append(n.val)
            n = n.next
        print(res)

    def mergeSortedLinkList(self, root1, root2):
        res = LinkNone(0)
        res1 = res
        while root1 and root2:
            if not root1:
                res1.next = root2
                return res
            elif not root2:
                res.next = root1
                return res
            else:
                if root1.val >= root2.val:
                    res1.next = LinkNone(root2.val)
                    root2 = root2.next
                    res1 = res1.next
                else:
                    res1.next = LinkNone(root1.val)
                    root1 = root1.next
                    res1 = res1.next
        return res

s = Solution()
s.show(s.mergeSortedLinkList(s.create([1,3,5,7,9]), s.create([2,4,6,8,10])))

