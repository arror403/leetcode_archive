class Solution:
    def largestLocal(self, g: List[List[int]]) -> List[List[int]]:
        l=len(g)-1
        res=[]
        for i in range(1,l):
            tmp=[]
            for j in range(1,l):
                tmp.append(max(g[i-1][j-1],g[i-1][j],g[i-1][j+1],
                               g[i][j-1],  g[i][j],  g[i][j+1],
                               g[i+1][j+1],g[i+1][j],g[i+1][j-1]))
            res.append(tmp)
        return res