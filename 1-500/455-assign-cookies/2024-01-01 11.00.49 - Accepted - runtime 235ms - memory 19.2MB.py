class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        ##### power by chatGPT #####

        g.sort()  # Sort the greed factors
        s.sort()  # Sort the cookie sizes
        res = 0
        
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                res += 1
                i += 1
            j += 1

        return res