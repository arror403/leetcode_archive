class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n=len(img),len(img[0])
        res=[[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                t=[i for i in chain.from_iterable(self.neighbors(img,i+1,j+1)) if i!=-1]
                # print(t)
                res[i][j]=floor(sum(t)/len(t))

        return res

    def neighbors(self, a, row_number, column_number):
        return [[a[i][j] if  i >= 0 and i < len(a) and j >= 0 and j < len(a[0]) else -1
                    for j in range(column_number-2, column_number+1)]
                        for i in range(row_number-2, row_number+1)]