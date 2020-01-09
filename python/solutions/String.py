# This file is leetcode problem for string topic

import collections

class Solution:
    def __init__(self):
        pass

    def kmp(self, s, p):
        '''
        :param s: str
        :param p: str
        :return: the index of the first occurrence of p in s
        '''
        Next = [-1] * len(p)
        if len(p)>1:
            Next[1] = 0
            i, j = 1, 0
            while i<len(p)-1:
                if j==-1 or p[i]==p[j]:
                    i += 1
                    j += 1
                    Next[i] = j
                else:
                    j = Next[j]
        i = j = 0
        while j<len(p) and i<len(s):
            if j==-1 or s[i]==p[j]:
                i += 1
                j += 1
            else:
                j = Next[j]

            if j==len(p):
                return i-j
        return -1

    def lengthOfLongestSubstring0003(self, s):
        res = 0
        left = 0
        cache = {}

        for ri, v in enumerate(s):
            if v in cache and cache[v] >= left:
                left = cache[v] + 1
            cache[v] = ri
            if ri-left+1 > res:
                res = ri-left+1
        return res

    def longestPalindrome0005(self, s):
        A = '@#' + '#'.join(s) + '#$'
        Z = [0] * len(A)
        c = r = 0
        for i in range(1, len(A) - 1):
            if i < r:
                Z[i] = min(r - i, Z[2 * c - i])
            while (A[i + Z[i] + 1] == A[i - Z[i] - 1]):
                Z[i] += 1
            if i + Z[i] > r:
                c, r = i, i + Z[i]
        print(A)
        maxlen = max(Z)
        center = Z.index(maxlen)
        res = A[center-maxlen: center+maxlen+1]
        return res.replace('#', '')

        # maxLen, start = 0, 0
        # for i in range(len(s)):
        #     if i - maxLen >= 1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]:
        #         start = i - maxLen - 1
        #         maxLen += 2
        #         continue
        #     if i - maxLen >= 0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
        #         start = i - maxLen
        #         maxLen += 1
        # res = s[start:start+maxLen]
        # return res


    def convert0006(self, s, numRows):
        n = numRows
        z = [''] * n
        while s:
            for i in range(n):
                if i < len(s):
                    z[i] += s[i]
                else:
                    break
            for i in range(n, 2*(n-1)):
                if i < len(s):
                    z[2*n-2-i] += s[i]
                else:
                    break
            s = s[2*(n-1):]
        res = ''.join(z)
        return res


    def isMatch0010(self, s: str, p: str) -> bool:
        if p == '.*':
            return True
        m, n = len(s), len(p)
        dp = [[False for i in range(n + 1)] for j in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i][j - 2] or (
                                dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                else:
                    dp[i][j] = dp[i - 1][j - 1] and p[j - 1] == s[i - 1]
        return dp[-1][-1]


    def intToRoman0012(self, num: int) -> str:
        res = ''
        while num >= 1000:
            res += 'M'
            num -= 1000
        if num >= 900:
            res += 'CM'
            num -= 900
        if num >= 500:
            res += 'D'
            num -= 500
        if num >= 400:
            res += 'CD'
            num -= 400
        while num >= 100:
            res += 'C'
            num -= 100
        if num >= 90:
            res += 'XC'
            num -= 90
        if num >= 50:
            res += 'L'
            num -= 50
        if num >= 40:
            res += 'XL'
            num -= 40
        while num >= 10:
            res += 'X'
            num -= 10
        if num >= 9:
            res += 'IX'
            num -= 9
        if num >= 5:
            res += 'V'
            num -= 5
        if num >= 4:
            res += 'IV'
            num -= 4
        while num > 0:
            res += 'I'
            num -= 1
        return res


    def romanToInt0013(self, s):
        res = 0
        if 'IV' in s or 'IX' in s:
            res -= 2
        if 'XL' in s or 'XC' in s:
            res -= 20
        if 'CD' in s or 'CM' in s:
            res -= 200
        for _s in s:
            if _s == 'M':
                res += 1000
            if _s == 'D':
                res += 500
            if _s == 'C':
                res += 100
            if _s == 'L':
                res += 50
            if _s == 'X':
                res += 10
            if _s == 'V':
                res += 5
            if _s == 'I':
                res += 1
        return res


    def longestCommonPrefix0014(self, strs):
        if len(strs) == 0:
            return ''
        # min_len = min([len(i) for i in strs])
        # if min_len == 0:
        #     return ''
        # res = ''
        # for i in range(min_len):
        #     st = strs[0][i]
        #     for s in strs:
        #         if s[i] != st:
        #             return res
        #     res += st
        # return res

        smin = min(strs)
        smax = max(strs)
        if smin == '':
            return ''
        for i, v in enumerate(smin):
            if smax[i] != smin[i]:
                return smin[:i]
        return smin

    def letterCombinations0017(self, digits):
        length = len(digits)
        if length == 0:
            return []
        dic = {'2': {'a', 'b', 'c'}, '3': {'d', 'e', 'f'}, '4': {'g', 'h', 'i'}, '5': {'j', 'k', 'l'},
               '6': {'m', 'n', 'o'}, '7': {'p', 'q', 'r', 's'}, '8': {'t', 'u', 'v'}, '9': {'w', 'x', 'y', 'z'}}
        res = []

        def helper(num, string, _res):
            if num == length:
                res.append(string)
                return
            for d in dic[digits[num]]:
                helper(num + 1, string + d, _res)

        helper(0, '', res)
        return res

    def groupAnagrams0049(self, strs):
        res = []
        temp = collections.defaultdict(list)
        for word in strs:
            count = sum(hash(x) for x in word)
            temp[count].append(word)
        for k, v in temp.items():
            res.append(v)
        return res

    def lengthOfLongestSubstringTwoDistinct0159(self, s):
        res, left, n = 0, 0, 0
        cache = {}
        for ri, v in enumerate(s):
            if v in cache and cache[v] >= left:
                cache[v] = ri
            elif n < 2:
                n += 1
            else:
                nse = s[ri - 1]
                for va in range(ri - 1, left - 1, -1):
                    if s[va] != nse:
                        se = va
                        break
                left = se + 1
            cache[v] = ri
            if ri - left + 1 > res:
                res = ri - left + 1
        return res


    def groupStrings0249(self, strings):
        res = []
        temp = collections.defaultdict(list)
        for word in strings:
            k = ""
            for i in range(1, len(word)):
                k += str((ord(word[i]) - ord(word[i - 1])) % 26)
            temp[k].append(word)
        for k, v in temp.items():
            res.append(v)
        return res


    def canPermutePalindrome0266(self, s):
        res = 0
        count = collections.Counter(s)
        for k, v in count.items():
            if v % 2 != 0:
                res += 1
        print(res < 2)
        return res < 2


    def lengthOfLongestSubstringKDistinct340(self, s, k):
        if k == 0: return 0
        res, left, n = 0, 0, 0
        cache = {}
        for ri, v in enumerate(s):
            if v in cache and cache[v] >= left:
                cache[v] = ri
            elif n < k:
                n += 1
            else:
                nse = set(s[ri - 1])
                x, se = 1, ri - 1
                for va in range(ri - 1, left - 1, -1):
                    if s[va] not in nse:
                        x += 1
                        if x >= k:
                            se = va
                            break
                        nse.add(s[va])
                left = se + 1
            cache[v] = ri
            if ri - left + 1 > res:
                res = ri - left + 1
        return res


    def longestPalindrome0409(self, s):
        res = 0
        count = collections.Counter(s)
        for k, v in count.items():
            if v % 2 != 0:
                res = res + v - 1
            else:
                res += v
        return res if res == len(s) else res + 1


    def characterReplacement0424(self, s, k):
        if not s: return 0

        left = -1
        cache = collections.defaultdict(lambda :0)
        n, res = 0, 0

        for i,v in enumerate(s):
            cache[v] += 1
            if n < cache[v]:
                n = cache[v]
            if i-left-n > k:
                res = max(i - left - 1, res)
                left += 1
                cache[s[left]] -= 1
        res = max(res, len(s)-1-left)

        # res, left, n = 0, 0, 0
        # Cmax = s[0]
        # cache = collections.defaultdict(lambda: 0)
        # for ri, v in enumerate(s):
        #     if v == Cmax:
        #         cache[v] += 1
        #         Cmax = max(cache.items(), key=lambda x: x[1])[0]
        #     elif n < k:
        #         n += 1
        #         cache[v] += 1
        #         Cmax = max(cache.items(), key=lambda x: x[1])[0]
        #     else:
        #         cache[v] += 1
        #         Cmax, _n = max(cache.items(), key=lambda x: x[1])
        #         n = ri - left + 1 - _n
        #         if n > k:
        #             for i in range(left, ri):
        #                 cache[s[i]] -= 1
        #                 Cmax, _n = max(cache.items(), key=lambda x: x[1])
        #                 n = ri - i - _n
        #                 if n <= k:
        #                     left = i + 1
        #                     break
        #     if ri - left + 1 > res:
        #         res = ri - left + 1
        return res


    def findAnagrams0438(self, s, p):
        res, n = [], len(p)
        countp = sum(hash(x) for x in p)
        countemp = sum(hash(x) for x in s[:n])
        if countp == countemp:
            res.append(0)
        for i in range(1, len(s) - n + 1):
            countemp = countemp - hash(s[i - 1]) + hash(s[i + n - 1])
            if countemp == countp:
                res.append(i)
        return res


    def countSubstrings0647(self, s):
        n = len(s)
        # if n < 2:
        #     return n
        # dp = [[0]*n for _ in range(n)]
        # for _ in range(n-1):
        #     dp[_][_] = 1
        #     if s[_] == s[_+1]:
        #         dp[_][_+1] = 1
        # dp[n-1][n-1] = 1
        # for l in range(3, n+1):
        #     for i in range(n-l+1):
        #         if s[i] == s[i+l-1] and dp[i+1][i+l-2] == 1:
        #             dp[i][i+l-1] = 1
        # res = sum(map(sum, dp))

        res, i = 0, 0
        while i < n:
            j, k = i, i
            while k < n-1 and s[k] == s[k+1]:
                k += 1
            res += (k-j+1)*(k-j+2)//2
            i = k+1
            j -= 1
            k += 1
            while j>-1 and k<n and s[j]==s[k]:
                res += 1
                j -= 1
                k += 1
        return res

    def test(self):
        # res = self.kmp_match('ababa')

        res = self.kmp_match('abababacasab', 'ABCDABD')
        # res = self.longestPalindrome0005('b')
        print(res)

sol = Solution()
sol.test()