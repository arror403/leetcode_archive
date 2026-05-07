class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        for a,b in zip(s,t):
            if a not in d.keys():
                if b in d.values(): return 0  # If b is already mapped to another character
                d[a]=b
            elif b!=d[a]:
                return 0

        return 1



        # if len(set(s))==1 and set(s)==set(t):
        #     return 1
        # elif sorted(s)==sorted(t):
        #     return 0
        # else:
        #     return Counter(s).values()==Counter(t).values()