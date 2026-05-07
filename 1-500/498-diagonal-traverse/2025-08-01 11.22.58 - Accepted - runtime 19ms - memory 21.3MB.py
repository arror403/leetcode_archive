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
        
        for diag in d.items():
            if diag[0]%2:
                [res.append(x) for x in diag[1]]
            else:
                [res.append(x) for x in diag[1][::-1]]
                

        return res



        # m,n=len(mat),len(mat[0])
        # res=[]

        # for i in range(m+n-1):
        #     for j in range(i+1):
        #         print(mat[j][i-j])
        #         res.append(mat[j][i-j])


        # return res