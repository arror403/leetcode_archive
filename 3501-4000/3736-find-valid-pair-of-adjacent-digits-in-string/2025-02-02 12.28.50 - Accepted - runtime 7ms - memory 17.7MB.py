class Solution:
    def findValidPair(self, s: str) -> str:
        d = Counter(s)

        for a, b in pairwise(s):
            if a != b and d[a] == int(a) and d[b] == int(b):
                return a+b

        return ""