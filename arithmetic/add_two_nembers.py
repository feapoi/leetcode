# problem：
#  两个链表代表两个数的各个位数，相加，合并成一个链表
#  例 (2 -> 4 -> 3) + (5 -> 6 -> 4)
#  结果 7 -> 0 -> 8
#
# solution:
#
#
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class AddTwoNembers:
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode(0)
        dummy = l3
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            sum = carry
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            carry = int(sum / 10)
            l3.next = ListNode(sum % 10)
            l3 = l3.next
        return dummy.next

    def create(self, n):
        l = ListNode(0)
        dummy = l
        for i in range(len(n)):
            l.next = ListNode(n[i])
            l = l.next
        return dummy.next

a1 = AddTwoNembers()
a2 = a1.create([4,6,8])
b1 = AddTwoNembers()
b2 = a1.create([3,2,1])
c1 = AddTwoNembers()
c2 = c1.addTwoNumbers(a2, b2)
print(c2.val, c2.next.val, c2.next.next.val)