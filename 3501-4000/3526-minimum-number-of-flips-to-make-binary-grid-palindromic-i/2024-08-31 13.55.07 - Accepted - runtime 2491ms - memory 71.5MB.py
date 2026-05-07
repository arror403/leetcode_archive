class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        return min(sum(sum(x^y for x,y in zip(r,r[::-1])) for r in grid), sum(sum(x^y for x,y in zip(c,c[::-1])) for c in zip(*grid)))//2