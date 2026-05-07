class Solution:
    def scoreOfString(self, s: str) -> int:
        d={c:v for v,c in enumerate('abcdefghijklmnopqrstuvwxyz')}
        return sum(abs(d[a]-d[b]) for a,b in pairwise(s))