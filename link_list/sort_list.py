# 排序一个链表，归并排序
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def create(self, n):
        l = ListNode(0)
        m = l
        for i in n:
            m.next = ListNode(i)
            m = m.next
        return l.next

    def show(self, n):
        res = []
        while n:
            res.append(n.val)
            n = n.next
        print(res)



    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        else:
            head2, tail = head, head
            head1 = head
            while tail and tail.next:
                head1 = head2
                head2 = head2.next
                tail = tail.next.next
            head1.next = None
            res1 = self.sortList(head)
            res2 = self.sortList(head2)
            res = ListNode(0)
            resTemp = res
            while res1 and res2:
                if res1.val > res2 .val:
                    resTemp.next = ListNode(res2 .val)
                    res2 = res2.next
                else:
                    resTemp.next = ListNode(res1 .val)
                    res1 = res1.next
                resTemp = resTemp.next
            if res1:
                resTemp.next = res1
            else:
                resTemp.next = res2
            return res.next


s = Solution()
s.show(s.sortList(s.create([6,3,1,4,7,8])))