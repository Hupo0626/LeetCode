# This file is leetcode problem for Array topic

import collections
from bisect import bisect_left, bisect_right

class Solution:
    def __init__(self):
        pass

    def twoSum0001(self, nums, target):
        # Brute Force O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        temp = {}
        for i, v in enumerate(nums):
            if v in temp:
                return [temp[v], i]
            temp[target - v] = i

    def findMedianSortedArrays0004(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        length = len(nums)
        return (nums[length // 2] + nums[(length - 1) // 2]) / 2

    def maxArea0011(self, height):
        head, tail = 0, len(height) - 1
        area, max_area = 0, 0
        while head < tail:
            l, r = height[head], height[tail]
            n = tail - head
            if l < r:
                area = l * n
                while height[head] <= l:
                    head += 1
            else:
                area = r * n
                while tail > -1 and height[tail] <= r:
                    tail -= 1
            if area > max_area:
                max_area = area
        return max_area

    def threeSum0015(self, nums):
        if len(nums) < 3:
            return []
        res = []
        keys = sorted(list(set(nums)))
        count = collections.Counter(nums)
        if count[0] >= 3:
            res.append([0, 0, 0])
        a_min = bisect_left(keys, -2 * keys[-1])
        a_max = bisect_left(keys, 0)
        for ai in range(a_min, a_max):
            a = keys[ai]
            if count[a] >= 2 and -a * 2 in count:
                res.append([a, a, -a * 2])
            b_min = max(ai + 1, bisect_left(keys, -a - keys[-1]))
            b_max = bisect_right(keys, -a // 2)
            for bi in range(b_min, b_max):
                b = keys[bi]
                c = -a - b
                if b <= c and c in count:
                    if b < c or count[b] >= 2:
                        res.append([a, b, c])
        return res

    def threeSumClosest0016(self, nums, target):
        nums.sort()
        p = set()
        for i in range(len(nums)-2):
            j,k = i+1, len(nums)-1
            if nums[i]+nums[j]+nums[j+1] > target:
                p.add(nums[i]+nums[j]+nums[j+1])
            elif nums[i]+nums[k-1]+nums[k] < target:
                p.add(nums[i]+nums[k-1]+nums[k])
            else:
                while j<k:
                    tmp = nums[i]+nums[j]+nums[k]
                    if tmp == target:
                        return tmp
                    p.add(tmp)
                    if tmp > target:
                        k -= 1
                    else:
                        j += 1
        return min(p, key=lambda x: abs(target-x))

    def fourSum0018(self, nums, target):
        if len(nums) < 4:
            return []
        keys = sorted(list(set(nums)))
        count = collections.Counter(nums)
        res = []
        fo = target // 4
        if fo in count and count[fo] >= 4 and fo * 4 == target:
            res.append([fo, fo, fo, fo])
        a_min = bisect_left(keys, target - 3 * keys[-1])
        a_max = bisect_right(keys, target // 4)
        for ai in range(a_min, a_max):
            a = keys[ai]
            if count[a] >= 2:
                if count[a] >= 3:
                    d = target - 3 * a
                    if target - 3 * a in count and d > a:
                        res.append([a, a, a, target - 3 * a])
                c_min = max(ai + 1, bisect_left(keys, target - 2 * a - keys[-1]))
                c_max = bisect_right(keys, (target - 2 * a) // 2)
                for ci in range(c_min, c_max):
                    c = keys[ci]
                    d = target - 2 * a - c
                    if count[c] >= 2 and d == c:
                        res.append([a, a, c, c])
                    if d > c and d in count:
                        res.append([a, a, c, d])
            b_min = max(ai + 1, bisect_left(keys, target - a - 2 * keys[-1]))
            b_max = bisect_right(keys, (target - a) // 3)
            for bi in range(b_min, b_max):
                b = keys[bi]
                if count[b] >= 2:
                    d = target - a - 2 * b
                    if count[b] >= 3 and d == b:
                        res.append([a, b, b, b])
                    elif d > b and d in count:
                        res.append([a, b, b, d])
                c_min = max(bi + 1, bisect_left(keys, target - a - b - keys[-1]))
                c_max = bisect_right(keys, (target - a - b) // 2)
                for ci in range(c_min, c_max):
                    c = keys[ci]
                    d = target - a - b - c
                    if d == c and count[c] >= 2:
                        res.append([a, b, c, c])
                    if d > c and d in count:
                        res.append([a, b, c, d])
        return res

    def removeDuplicates0026(self, nums):
        if len(nums) == 0:
            return 0
        cur_i = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[cur_i]:
                cur_i += 1
                nums[cur_i] = nums[i]
        return cur_i + 1

    def removeElement0027(self, nums, val):
        i = 0
        for j, v in enumerate(nums):
            if v != val:
                nums[i] = v
                i += 1
        return i

    def nextPermutation0031(self, nums):
        r = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                r = i
                break
        if r == -1:
            nums.sort()
        else:
            for j in range(len(nums) - 1, r, -1):
                if nums[j] > nums[r]:
                    nums[j], nums[r] = nums[r], nums[j]
                    nums[r + 1:] = sorted(nums[r + 1:])
                    break

    def search0033(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 or target not in set(nums):
            return -1
        head = nums[0]
        if head == target:
            return 0
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            mid = nums[m]
            if mid == target:
                return m
            if mid == head:
                l = m + 1
            else:
                if mid < head < target or target < mid < head or head < target < mid:
                    r = m
                elif mid < target < head or head < mid < target or target < head < mid:
                    l = m + 1
        return l

    def searchRange0034(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in set(nums):
            return [-1, -1]
        if len(nums) == 1:
            return [0, 0]
        l, r = 0, len(nums) - 1
        m = (l + r) // 2
        while l < r:
            mid = nums[m]
            if mid == target:
                break
            if mid > target:
                r = m
            else:
                l = m + 1
            m = (l + r) // 2
        ll, lr = l, m
        rl, rr = m, r
        while ll < lr:
            lm = (ll + lr) // 2
            if nums[lm] == target:
                lr = lm
            elif nums[lm] < target:
                ll = lm + 1
        while rl < rr:
            rm = (rl + rr) // 2
            if nums[rm] == target:
                rl = rm + 1
            elif nums[rm] > target:
                rr = rm - 1
        if nums[rr] > target:
            rr -= 1
        return [ll, rr]

    def searchInsert0035(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        m = (l + r) // 2
        while l <= r:
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
            m = (l + r) // 2
        return l
        # return bisect_left(nums, target)

    def combinationSum0039(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        candidates.sort()
        self.helper0039(candidates, 0, [], target)
        return self.res

    def helper0039(self, candidates, start, items, target):
        if target == 0:
            self.res.append(items)
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return
            self.helper0039(candidates, i, items + [candidates[i]], target - candidates[i])

    def combinationSum0040(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        candidates.sort()
        self.helper0040(0, [], target, candidates)
        return self.res

    def helper0040(self, start, items, target, candidates):
        if target == 0:
            self.res.append(items)
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return
            if i == start or candidates[i] != candidates[i - 1]:
                self.helper0040(i + 1, items + [candidates[i]], target - candidates[i], candidates)

    def trap0042(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0
        l, r = 0, len(height) - 1
        l_h, r_h = height[l], height[r]
        res = 0
        while l < r:
            while height[l] <= height[r] and l < r:
                if height[l] > l_h:
                    l_h = height[l]
                res += l_h - height[l]
                l += 1
            while height[l] > height[r] and l < r:
                if height[r] > r_h:
                    r_h = height[r]
                res += r_h - height[r]
                r -= 1
        return res

    def jump0045(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums.count(1) == len(nums):
            return len(nums) - 1
        if len(nums) < 2:
            return 0
        res = 1
        cur, far = 0, nums[0]
        while far < len(nums) - 1:
            res += 1
            # nxt = max(i+nums[i] for i in range(cur, far+1))
            # cur, far = far, nxt
            _m = cur + nums[cur]
            _i = cur
            for i in range(cur + 1, far + 1):
                if i + nums[i] > _m:
                    _m = i + nums[i]
                    _i = i
            cur, far = _i, _m
        return res

    def rotate0048(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = zip(*matrix[::-1])

        # n = len(matrix)
        # for i in range(n // 2):
        #     for j in range(i, n - 1 - i):
        #         matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = \
        #         matrix[n - 1 - j][i], matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j]

    def maxSubArray0053(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = s = nums[0]
        for num in nums[1:]:
            s = s + num if s>0 else num
        if s>res:
            res = s
        return res

    def spiralOrder0054(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        _res = []
        while matrix:
            _res.append(matrix.pop(0))
            matrix = list(zip(*matrix))[::-1]
        return [x for _list in _res for x in _list]

        # if len(matrix)==0:
        #     return []
        # m,n = len(matrix)-1, len(matrix[0])-1
        # l,r,d,u = 0,n,m,0
        # res = []
        # direct = 0
        # while l<=r and u<=d:
        #     if direct==0:
        #         for j in range(l,r+1):
        #             res.append(matrix[u][j])
        #         u += 1
        #     if direct==1:
        #         for i in range(u,d+1):
        #             res.append(matrix[i][r])
        #         r -= 1
        #     if direct==2:
        #         for j in range(r,l-1,-1):
        #             res.append(matrix[d][j])
        #         d -= 1
        #     if direct==3:
        #         for i in range(d,u-1,-1):
        #             res.append(matrix[i][l])
        #         l += 1
        #     direct = (direct+1)%4
        # return res

    def canJump0055(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_dis = 0
        for i, n in enumerate(nums):
            if i + n > max_dis:
                max_dis = i + n
            if max_dis <= i and i < len(nums) - 1:
                return False
        return True

    def merge0056(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)
        return res

    def insert0057(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals:
            return [newInterval]
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)
        return res

    def advantageCount0870(self, A, B):
        # res = []
        # sortA, sortB = sorted(A), sorted(B)
        #
        # assigned = {b: [] for b in B}
        # remain = []
        #
        # i = 0
        # for a in sortA:
        #     if a > sortB[i]:
        #         assigned[sortB[i]].append(a)
        #         i += 1
        #     else:
        #         remain.append(a)
        #
        # for b in B:
        #     if assigned[b]:
        #         res.append(assigned[b].pop())
        #     else:
        #         res.append(remain.pop())

        n = len(A)
        res = [0 for i in range(n)]
        sortA = sorted(A)
        low, high = 0, n-1
        sortinxB = sorted(range(n), key=lambda x: B[x], reverse=True)

        for i in sortinxB:
            if sortA[high]>B[i]:
                res[i] = sortA[high]
                high -= 1
            else:
                res[i] = sortA[low]
                low += 1

    def videoStitching(self, clips, T):
        dic = collections.defaultdict(list)
        res = 101
        for c in clips:
            dic[c[0]].append(c[1])
        cmax = max(clips, key=lambda x:x[1])
        cmax = cmax[1]
        if cmax<T or 0 not in dic:
            return -1
        count = 0
        v = 0
        dmax = max(dic[0])
        count += 1
        while dmax<T:
            ov = v
            v = dmax
            for i in range(ov+1,v+1):
                if i not in dic:
                    continue
                dmax = max(dmax, max(dic[i]))
            count += 1
        res = min(count, res)
        return res

    def test(self):
        # add the function that you want to test here
        pass


sol = Solution()
sol.test()