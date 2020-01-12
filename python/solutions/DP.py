# This file is leetcode problem for Dynamic Programming topic

class Solution:
    def __init__(self):
        pass

    def canCross403(self, stones):
        if stones[1] != 1:
            return False
        if stones[-1] - stones[-2] > 1100:
            return False
        last = stones[-1]
        stones = set(stones)
        temp = [(1, 1)]
        while temp:
            key, step = temp.pop()
            if key == last:
                return True
            k_set = (1, 2) if step == 1 else (step - 1, step, step + 1)
            for k in k_set:
                if key + k in stones:
                    temp.append((key + k, k))
        return False

        # temp = {s: set() for s in stones}
        # temp[0].add(0)
        # for key in stones[:-1]:
        #     for v in temp[key]:
        #         for k in (v - 1, v, v + 1):
        #             if k > 0 and key + k in temp:
        #                 temp[key + k].add(k)
        # return bool(temp[stones[-1]])

    def test(self):
        intervals = [(1,2),(3,5),(12,19)]
        print(sorted(list(k[0] for k in intervals)))
        # print(l)

sol = Solution()
sol.test()