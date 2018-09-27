class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def cyclic(self, list):
        a = list
        b = list
        flag = 0
        while a.next != None and b.next.next != None:
            a = a.next
            b = b.next.next
            if a == b:
                flag = 1
                print("exist cyclic")
                return a
        if flag == 1:
            a = list
            while a != b:
                a = a.next
                b = b.next
            return a

        print("not exist cyclic")
        return False

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
print(s.cyclic(node1).val)