# This file is leetcode problem for ListNode topic


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


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

    def removeNthFromEnd0019(self, head: ListNode, n: int) -> ListNode:
        pre = None
        rem = cur = head
        i = 1
        while i<n:
            cur = cur.next
            i += 1
        while cur.next:
            cur = cur.next
            pre = rem
            rem = rem.next
        if pre:
            pre.next = rem.next
            return head
        return head.next

    def mergeTwoLists0021(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dum = ListNode(0)
        cur = dum
        while l1 and l2:
            if l1.val<l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dum.next

    def mergeKLists0023(self, lists: list[ListNode]) -> ListNode:
        nums = []
        for l in lists:
            while l:
                nums.append(l)
                l = l.next
        dum = ListNode(0)
        cur = dum
        for n in sorted(nums, key=lambda x:x.val):
            cur.next = n
            cur = cur.next
        return dum.next

    def swapPairs0024(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            tmp = cur.val
            cur.val = cur.next.val
            cur.next.val = tmp
            cur = cur.next.next
        return head

    def flatten0430(self, head: 'Node') -> 'Node':
        tmp = []
        cur = head
        while cur:
            if cur.child:
                if cur.next:
                    tmp.append(cur.next)
                    cur.next.prev = None
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None
            elif not cur.next and tmp:
                cur.next = tmp.pop()
                cur.next.prev = cur
            cur = cur.next
        return head

    def test(self):
        self.addTwoNumbers0002(self.l1, self.l2)

sol = Solution()
sol.test()