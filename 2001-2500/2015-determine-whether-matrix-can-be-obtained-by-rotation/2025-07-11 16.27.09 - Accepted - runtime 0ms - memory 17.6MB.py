class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat==target: return True
        
        for _ in range(3):
            m=[[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0])-1,-1,-1)]
            if m==target: return True
            else: mat=m

        return False