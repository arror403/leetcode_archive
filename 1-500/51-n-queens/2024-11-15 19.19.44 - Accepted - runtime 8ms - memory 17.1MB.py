# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         res=[]
#         nQueens=['.']*n
#         flag=[1]*(5*n-2)
#         self.solver(res, nQueens, flag, 0, n)
#         return res

#     def solver(self, res, nQueens, flag, row, n):
#         if row==n:
#             res.append(nQueens)
#             return

#         col=0
#         while col!=n:
#             if (flag[col] and flag[n+row+col] and flag[4*n-2+col-row]):
#                 flag[col]=flag[n+row+col]=flag[4*n-2+col-row]=0
#                 nQueens[row][col]='Q'
#                 self.solver(res, nQueens, flag, row+1, n)
#                 nQueens[row][col]='.'
#                 flag[col]=flag[n+row+col]=flag[4*n-2+col-row]=1
#             col+=1

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        nQueens=[['.']*n for _ in range(n)]
        flag=[1]*(5*n-2)
        
        self.solver(res, nQueens, flag, 0, n)
        return res
    

    def solver(self, res, nQueens, flag, row, n):
        if row==n:
            # Convert the current board state to the required string format
            res.append([''.join(row) for row in nQueens])
            return
        
        for col in range(n):
            # Check if the current position is safe
            # col: checks column
            # n+row+col: checks positive diagonal
            # 4*n-2+col-row: checks negative diagonal
            if (flag[col] and flag[n+row+col] and flag[4*n-2+col-row]):
                # Mark the position as under attack
                flag[col]=flag[n+row+col]=flag[4*n-2+col-row]=0
                # Place the queen
                nQueens[row][col]='Q'
                
                # Move to next row
                self.solver(res, nQueens, flag, row + 1, n)
                
                # Backtrack: remove the queen and clear attack markers
                nQueens[row][col]='.'
                flag[col]=flag[n+row+col]=flag[4*n-2+col-row]=1