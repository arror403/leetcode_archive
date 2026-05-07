class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n=len(img),len(img[0])

        def neighbors(row_number, column_number):
            return [[img[i][j] if i>=0 and i<m and j>=0 and j<n else -1
                    for j in range(column_number-2, column_number+1)]
                    for i in range(row_number-2, row_number+1)]
        
        res=[[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                t=[i for i in [y for x in neighbors(i+1,j+1) for y in x] if i!=-1]
                res[i][j]=floor(sum(t)/len(t))

        return res