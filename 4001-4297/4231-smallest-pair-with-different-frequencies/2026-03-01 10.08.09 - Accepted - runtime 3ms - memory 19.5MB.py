class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        d=Counter(nums)
        t=sorted(d.keys())
        L=len(t)

        for i in range(L):
            for j in range(i+1, L):
                if d[t[i]] != d[t[j]]:
                    return [t[i], t[j]]


        return [-1, -1]