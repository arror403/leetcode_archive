class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k=(k%(len(mat[0])))*(-1)
        for i in range(len(mat)):
            k*=-1
            if (mat[i][k:]+mat[i][:k])!=mat[i]:
                return False

        return True