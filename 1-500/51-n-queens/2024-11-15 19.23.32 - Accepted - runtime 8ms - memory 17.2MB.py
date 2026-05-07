class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        nQueens=[['.']*n for _ in range(n)]
        flag=[1]*(5*n-2)

        def solver(res, nQueens, flag, row, n):
            if row==n:
                res.append([''.join(row) for row in nQueens])
                return

            for col in range(n):
                if (flag[col] and flag[n+row+col] and flag[4*n-2+col-row]):
                    flag[col]=flag[n+row+col]=flag[4*n-2+col-row]=0
                    nQueens[row][col]='Q'
                    solver(res, nQueens, flag, row+1, n)
                    nQueens[row][col]='.'
                    flag[col]=flag[n+row+col]=flag[4*n-2+col-row]=1
                col+=1

        solver(res, nQueens, flag, 0, n)


        return res