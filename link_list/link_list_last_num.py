#  找出链表倒数第n个数
class LinkNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def create(self, n):
        l = LinkNode(0)
        m = l
        for i in n:
            l.next = LinkNode(i)
            l = l.next
        return m

    def show(self, n):
        res = []
        n = n.next
        while n:
            res.append(n.val)
        print(res)

    # 第一种方法：利用两个Node a1 s2，从root开始，当a1 next到n的时候,
    # a2 开始走，a1到达终点，a2的位置val就是目标值
    def linkListLastNum1(self, root, targetNum):
        a1 = root
        a2 = root
        for i in range(targetNum):
            if a1:
                a1 = a1.next
            else:
                return None
        while a1:
            a1 = a1.next
            a2 = a2.next
        return a2.val

    # 第一种方法：a1走完整个长度，算出目标位置，a2走到对应的位置
    def linkListLastNum2(self, root, targetNum):
        len = 0
        a1 = root
        while a1:
            len += 1
            a1 = a1.next
        len = len - targetNum
        while len:
            len -= 1
            root = root.next
        return root.val

s = Solution()
print(s.linkListLastNum2(s.create([1,2,3,4,5,6,7]), 6))






