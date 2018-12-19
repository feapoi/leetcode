class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def create(self, n):
        l = ListNode(0)
        dummy = l
        for i in range(len(n)):
            l.next = ListNode(n[i])
            l = l.next
        return dummy.next

    def show(self, l):
        while l.next:
            print(l.val)
            l = l.next
        print(l.val)

    # 一个个拆:
    # 使用a1和a2两个指针配合工作，使得两个节点间的指向反向，同时用r记录剩下的链表。
    def reversal_1(self, head):
        if not head or not head.next:
            return head
        a1 = head
        a2 = head.next
        head.next = None
        print(a1.next)
        while a2:
            r = a2.next
            a2.next = a1
            a1 = a2
            a2 = r
        return a1

    ## 递归
    def reversal_3(self, head):
        if head.next == None:
            return head
        new_head = self.reversal_3(head.next)
        head.next.next = head
        head.next = None
        return new_head


s = Solution()
b1 = s.create([1,2,3,4,5,6])
s.show(s.reversal_3(b1))


