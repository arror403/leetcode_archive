class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        return sum([mat[i][j] for i,r in enumerate(mat) if sum(r)==1 for j,c in enumerate(zip(*mat)) if sum(c)==1])