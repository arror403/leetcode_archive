class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        a,b=0,0

        for r in grid: a+=sum(x^y for x,y in zip(r,r[::-1]))
        for c in zip(*grid): b+=sum(x^y for x,y in zip(c,c[::-1]))

        return min(a//2, b//2)