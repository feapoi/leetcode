from queue import PriorityQueue
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    ## 利用优先队列比较
    def mergeKLists1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        no = 0
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                no += 1
                q.put((l.val, no, l))
        while not q.empty():
            val, this_no, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, this_no, node))
        return head.next

    ## 直接比较
    def mergeKLists2(self, list1, list2):
        head = point = ListNode(0)
        if list1 == None and list2 == None:
            return head
        while list1 != None or list2 != None:
            if list1 != None and list2 != None:
                if list1.val > list2.val:
                    point.next = list2
                    point = point.next
                    list2 = list2.next
                else:
                    point.next = list1
                    point = point.next
                    list1 = list1.next
            elif list1 != None:
                point.next = list1
                point = point.next
                return head.next
            elif list2 != None:
                point.next = list2
                point = point.next
                return head.next
            else:
                return head.next
        return head.next

    ##递归
    def mergeKLists3(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeKLists3(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeKLists3(l1, l2.next)
            return l2


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

s = Solution()
a2 = s.create([1,4,5])
b2 = s.create([1,3,4])
c2 = s.mergeKLists3(a2, b2)
s.show(c2)


