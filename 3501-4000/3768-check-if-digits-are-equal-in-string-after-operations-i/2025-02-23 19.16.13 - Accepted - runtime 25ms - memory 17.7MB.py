class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s=[int(x) for x in s]

        while len(s)>2:
            s=[(a+b)%10 for a,b in pairwise(s)]

        return s[0]==s[1]