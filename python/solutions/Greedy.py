# This file is leetcode problem for Array topic


class Solution:
    def __init__(self):
        pass

    def twoCitySchedCost1029(self, costs: list[list[int]]) -> int:
        costs = sorted(costs, key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        return sum(cost[0] for cost in costs[:n]) + sum(cost[1] for cost in costs[n:])

    def test(self):
        # add the function that you want to test here
        pass


sol = Solution()
sol.test()