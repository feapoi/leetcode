# problem：
#  判断一个链表是否是回文的
#  例     [1,2,1]
#  结果   True
#
# solution
# deque
import collections
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        all_list = collections.deque()
        t = head
        while t:
            all_list.append(t.val)
            t = t.next
        while all_list:
            r = all_list.pop()
            if not all_list:
                break
            l = all_list.popleft()
            if r != l:
                return False
        return True

