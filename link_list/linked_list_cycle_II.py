# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        cur, front = head, head
        while front and front.next:
            cur = cur.next
            front = front.next.next
            if front == cur:
                break
        if not front or not front.next:
            return None
        cur = head
        idx = 0
        while cur != front:
            cur = cur.next
            front = front.next
            idx += 1

        return cur

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2
s = Solution()
print(s.detectCycle(node1))