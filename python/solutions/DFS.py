# This file is leetcode problem for DFS topic

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.isValidBST0098()

    def inOrder(self, root, arr):
        if not root:
            return
        self.inOrder(root.left, arr)
        arr.append(root.val)
        self.inOrder(root.right, arr)

    def ifValid(self, node, lower, upper):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            return self.ifValid(node.left, lower, node.val) and self.ifValid(node.right, node.val, upper)


    def isValidBST0098(self, root):
        temp = []
        self.inOrder(root, temp)
        for i in range(1, len(temp)):
            if temp[i] < temp[i-1]:
                return False
        return True
        # return self.ifValid(root, float('-inf'), float('inf'))

    def isSameTree0100(self, p, q):
        if p == None and q == None: return True
        if p and q and p.val == q.val:
            return self.isSameTree0100(p.left, q.left) and self.isSameTree0100(p.right, q.right)
        return False

    def maxDepth0104(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth0104(root.left), self.maxDepth0104(root.right))

    def sortedArrayToBST0108(self, nums):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            root = TreeNode(nums[0])
            return root
        root = TreeNode(nums[len(nums) // 2])
        root.left = self.sortedArrayToBST0108(nums[:len(nums) // 2])
        root.right = self.sortedArrayToBST0108(nums[len(nums) // 2 + 1:])
        return root

    def isBalanced0110(self, root):
        if not root:
            return True
        if abs(self.maxDepth0104(root.left) - self.maxDepth0104(root.right)) > 1:
            return False
        return self.isBalanced0110(root.left) and self.isBalanced0110(root.right)

    def minDepth0111(self, root):
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth0111(root.right)
        elif not root.right:
            return 1 + self.minDepth0111(root.left)
        else:
            return 1 + min(self.minDepth0111(root.left), self.minDepth0111(root.right))

    def hasPathSum0112(self, root, sum):
        if not root:
            return False
        elif not root.left and not root.right:
            return root.val == sum
        elif not root.left:
            return self.hasPathSum0112(root.right, sum - root.val)
        elif not root.right:
            return self.hasPathSum0112(root.left, sum - root.val)
        else:
            return self.hasPathSum0112(root.left, sum - root.val) or self.hasPathSum0112(root.right, sum - root.val)

    def pathSum0113(self, root, sum):
        if not root:
            return []
        res = []

        def path(root, arr, _sum):
            if not root.left and not root.right:
                if root.val == _sum:
                    res.append(arr)
            if root.right:
                path(root.right, arr + [root.right.val], _sum - root.val)
            if root.left:
                path(root.left, arr + [root.left.val], _sum - root.val)
        path(root, [root.val], sum)
        return res

    def flatten0114(self, root):
        if root:
            self.getflatten(root)

    def getflatten(self, root):
        if not root:
            return
        self.getflatten(root.left)
        self.getflatten(root.right)
        current = root.left
        if not current:
            return
        while current.right:
            current = current.right
        current.right = root.right
        root.right = root.left
        root.left = None

    def flatten0430(self, head):
        current = head
        while current:
            if current.child:
                currentNext = current.next
                currentChild = current.child
                while currentChild.next:
                    currentChild = currentChild.next
                currentChild.next = currentNext
                if currentNext:
                    currentNext.prev = currentChild
                current.next = current.child
                current.child.prev = current
                current.child = None
                current = current.next
            else:
                current = current.next
        return head

    def pathSum0437(self, root, sum):
        if not root:
            return 0
        res = self.path(root, sum)
        res += self.pathSum0437(root.right, sum)
        res += self.pathSum0437(root.left, sum)
        return res

    def path(self, root, _sum):
        if not root:
            return 0
        _res = (root.val == _sum)
        _res += self.path(root.right, _sum - root.val)
        _res += self.path(root.left, _sum - root.val)
        return _res

    def findMode0501(self, root):
        if not root:
            return []
        temp = []
        self.inOrder(root, temp)

        d = collections.Counter(temp)
        maxTimes = max(d.items(), key=lambda x: x[1])[1]
        return [k for k, v in d.items() if v == maxTimes]

    def maxDepth0559(self, root):
        if not root:
            return 0
        if not root.children:
            return 1
        return 1 + max(self.maxDepth0559(child) for child in root.children)

    def allPathsSourceTarget0797(self, graph: list[list[int]]) -> list[list[int]]:
        self.res0979 = []
        self.graph = graph
        self.helper0797(0, [0])
        return self.res0797

    def helper0797(self, start, cur_path):
        if start == len(self.graph) - 1:
            self.res0797.append(cur_path)
            return
        for y in self.graph[start]:
            self.helper0797(y, cur_path + [y])


    def test(self):
        res = self.longestPalindrome0005('b')
        print(res)

sol = Solution()
sol.test()