class Solution:
    def __init__(self):
        self.lenLongestFibSubseq873()

    def advantageCount870(self, A, B):
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

        print(res)
        return res

    def lenLongestFibSubseq873(self, A):




sol = Solution()
