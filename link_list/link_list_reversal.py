# 链表反转
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
        if head.next == None:
            return head
        head1 = head
        head2 = head.next
        head.next = None
        while head2:
            r = head2.next
            head2.next = head1
            head1 = head2
            head2 = r
        return head1

    ## 递归
    # 先找到头结点，倒序一个个往最后一个节点插
    def reversal_3(self, head):
        if head.next == None:
            return head
        new_head = self.reversal_3(head.next)
        # 递归 1 - 6到此
        head.next.next = head
        # 5 -> 6 -> None     =>
        # 5 -> None      6 -> 5 -> None

        # 下一个

        # 4 -> 5 > None   =>
        # 6 -> 5 -> 4
        head.next = None
        return new_head

s = Solution()
b1 = s.create([1,2,3,4,5,6])
s.reversal_3(b1)


