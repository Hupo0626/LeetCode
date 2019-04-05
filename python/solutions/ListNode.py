# This file is leetcode problem for ListNode topic

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.l1 = self.creatListNode([2, 4, 9, 9])
        self.l2 = self.creatListNode([5, 6, 4])

    def creatListNode(self, l):
        if not l:
            return None
        cur = head = ListNode(0)
        while l:
            cur.next = ListNode(l.pop(0))
            cur = cur.next
        return head.next

    def addTwoNumbers0002(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag, head = 0, ListNode(0)
        cur = head
        while l1 or l2 or flag:
            if l1:
                flag += l1.val
                l1 = l1.next
            if l2:
                flag += l2.val
                l2 = l2.next
            cur.next = ListNode(flag % 10)
            cur = cur.next
            flag //= 10
            while head.next:
                print(head.next.val)
                head = head.next
        return head.next

    def test(self):
        self.addTwoNumbers0002(self.l1, self.l2)

sol = Solution()
sol.test()