# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # hash
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        thisDict = dict()
        while headA:
            k = headA.val
            thisDict[k] = headA
            headA = headA.next
        while headB:
            if thisDict.get(headB.val) == headB:
                return headB
            headB = headB.next
        return None

    def getIntersectionNode1(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        headX = headA
        headY = headB
        x, y = False, False
        while headX or headY or not x or not y:
            if headX == headY:
                return headX
            else:
                if headX.next:
                    headX = headX.next
                else:
                    x = True
                    headX = headB
                if headY.next:
                    headY = headY.next
                else:
                    y = True
                    headY = headA
        return None