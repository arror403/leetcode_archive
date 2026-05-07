class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        for a,b in zip(s,t):
            if a not in d:
                if b in d.values():
                    return 0
                d[a]=b
            elif b!=d[a]:
                return 0

        return 1