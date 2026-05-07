class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row=[i for i,r in enumerate(mat) if sum(r)==1]
        col=[j for j,c in enumerate(zip(*mat)) if sum(c)==1]

        return sum(1 if mat[i][j]==1 else 0 for i in row for j in col)