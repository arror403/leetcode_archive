class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d={}
        res=[]

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i+j not in d:
                    d[i+j]=[mat[i][j]]
                else:
                    d[i+j].append(mat[i][j])
        
        for k,v in d.items(): res+=[x for x in v] if k%2 else [x for x in v[::-1]]
                

        return res