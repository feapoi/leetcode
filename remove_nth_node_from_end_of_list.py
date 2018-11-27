class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def show(self, l):
        while l.next:
            print(l.val)
            l = l.next
        print(l.val)
    def create(self, n):
        l = ListNode(0)
        dummy = l
        for i in range(len(n)):
            l.next = ListNode(n[i])
            l = l.next
        return dummy.next
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        a = head
        b = head
        i = 0
        while b != None:
            i += 1
            if b.next is None:
                if a.next is None:
                    a.next = None
                else:
                    a.next = a.next.next
                return head
            elif i <= n:
                b = b.next
            else:
                a = a.next
                b = b.next
s = Solution()
b1 = s.create([1,2,3,4])
s.show(s.removeNthFromEnd(b1, 2))