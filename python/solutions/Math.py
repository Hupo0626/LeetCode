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

    def divide0029(self, dividend: int, divisor: int) -> int:
        a = abs(dividend)
        b = abs(divisor)
        if a < b:
            return 0
        res = 0
        while a >= b:
            sum = b
            count = 1
            while 2 * sum <= a:
                sum += sum
                count += count
            a -= sum
            res += count
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = -res
        return res if res < 2 ** 31 - 1 else 2 ** 31 - 1

    def test(self):
        res = self.reverse0007(-3520)
        print(res)

sol = Solution()
sol.test()