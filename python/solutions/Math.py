# This file is leetcode problem for math topic

class Solution:
    def __init__(self):
        pass

    def reverse0007(self, x):
        x = str(x)
        prefix = '-' if x[0] == '-' else ''
        x = x.strip('-')[::-1]
        res = int(prefix + x)
        if res < -2147483648 or res > 2147483647:
            return 0
        return res

    def test(self):
        res = self.reverse0007(-3520)
        print(res)

sol = Solution()
sol.test()