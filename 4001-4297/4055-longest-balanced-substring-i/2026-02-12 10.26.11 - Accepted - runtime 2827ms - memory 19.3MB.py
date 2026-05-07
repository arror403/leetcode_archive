class Solution:
    def longestBalanced(self, s: str) -> int:
        L = len(s)
        res = 0

        for i in range(L):
            c = defaultdict(int)
            for j in range(i, L):
                c[s[j]] += 1
                if len(set(c.values())) == 1:
                    res = max(res, j-i+1)


        return res