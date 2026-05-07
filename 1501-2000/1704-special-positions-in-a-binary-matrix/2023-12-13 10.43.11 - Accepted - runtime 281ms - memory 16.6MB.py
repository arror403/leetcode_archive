class Solution:
    def numSpecial(self, m: List[List[int]]) -> int:
        return sum([1 for i,r in enumerate(m) for j,c in enumerate(zip(*m)) if r.count(1)==c.count(1)==m[i][j]==1])