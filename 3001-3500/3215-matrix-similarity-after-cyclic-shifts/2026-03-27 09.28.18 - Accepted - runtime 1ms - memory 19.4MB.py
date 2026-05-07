class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m,n=len(mat),len(mat[0])
        k=(k%n)*(-1)
        t=[]
        for i in range(m):
            k*=-1
            t.append(mat[i][k:]+mat[i][:k])      

        return t==mat