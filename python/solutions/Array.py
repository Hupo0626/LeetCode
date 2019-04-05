# This file is leetcode problem for Array topic

import collections
from bisect import bisect_left, bisect_right

class Solution:
    def __init__(self):
        pass

    def twoSum0001(self, nums, target):
        temp = {}
        for i, v in enumerate(nums):
            if v in temp:
                return [temp[v], i]
            temp[target - v] = i


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
        count = collections.Counter(nums)
        keys = list(count.keys())
        keys.sort()
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
        p = []
        N = len(nums)
        for i in range(N-2):
            j,k = i+1, N-1
            if nums[i]+nums[j]+nums[j+1] > target:
                p.append(nums[i]+nums[j]+nums[j+1])
            elif nums[i]+nums[k-1]+nums[k] < target:
                p.append(nums[i]+nums[k-1]+nums[k])
            else:
                while j<k:
                    tmp = nums[i]+nums[j]+nums[k]
                    if tmp == target:
                        return tmp
                    p.append(tmp)
                    if tmp > target:
                        k -= 1
                    else:
                        j += 1
        return min(p, key=lambda x: abs(target-x))

    def fourSum0018(self, nums, target):
        if len(nums) < 4:
            return []
        res = []
        count = collections.Counter(nums)
        keys = list(count.keys())
        keys.sort()
        hi = keys[-1]
        fo = target//4
        if fo in count and fo*4==target:
            if count[fo]>=4:
                res.append([fo,fo,fo,fo])
        a_min = bisect_left(keys,target-3*hi)
        a_max = bisect_right(keys,target//4+1)
        for ai in range(a_min, a_max):
            a = keys[ai]
            dp = target-3*a
            if count[a]>=3 and dp in count and dp>a:
                res.append([a,a,a,dp])
            cd = target-2*a
            if count[a]>=2:
                for ci in range(max(ai+1,bisect_left(keys, cd-hi)), bisect_right(keys, cd//2+1)):
                    c = keys[ci]
                    d = target-a*2-c
                    if c<=d and d in count:
                        if c<d or count[c]>=2:
                            res.append([a,a,c,d])
            b_min = max(ai+1, bisect_left(keys, target-a-2*hi))
            b_max = bisect_right(keys, (target-a)//3+1)
            for bi in range(b_min, b_max):
                b = keys[bi]
                if count[b]>=3:
                    if a+3*b==target:
                        res.append([a,b,b,b])
                if count[b]>=2:
                    d = target-a-b*2
                    if b<d and d in count:
                        res.append([a,b,b,d])
                c_min = max(bi+1, bisect_left(keys, target-a-b-hi))
                c_max = bisect_right(keys, (target-a-b)//2+1)
                for ci in range(c_min, c_max):
                    c = keys[ci]
                    d = target-a-b-c
                    if c<=d and d in count:
                        if c<d or count[c]>=2:
                            res.append([a,b,c,d])
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

    def test(self):
        nums = [-1, 2, 1, -4]
        res = self.threeSumClosest0016(nums, 1)
        print(res)


sol = Solution()
sol.test()