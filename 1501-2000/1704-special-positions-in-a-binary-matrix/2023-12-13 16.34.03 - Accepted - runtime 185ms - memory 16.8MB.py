class Solution:
    def numSpecial(self, m: List[List[int]]) -> int:
        return sum([m[i][j] for i,r in enumerate(m) if sum(r)==1 for j,c in enumerate(zip(*m)) if sum(c)==1])