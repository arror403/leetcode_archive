class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        m = 0

        for i in range(n):
            c={}
            for j in range(i, n):
                c[s[j]] = c.get(s[j], 0) + 1

                if len(set(c.values())) == 1:
                    m = max(m, j-i+1)


        return m