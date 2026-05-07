class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        rows, cols = len(m), len(m[0])
        res = [0] * cols  # Initialize the result list with zeros

        for i in range(cols):
            res[i] = m[0][i]  # Initialize the first row of result with the values from the first row of the matrix

        for row in range(1, rows):  # Start from the second row
            temp_res = [0] * cols  # Initialize a temporary result list for the current row

            for col in range(cols):
                # Update the temporary result with the minimum value from the previous row
                if col == 0:
                    temp_res[col] = m[row][col] + min(res[col], res[col + 1])
                elif col == cols - 1:
                    temp_res[col] = m[row][col] + min(res[col - 1], res[col])
                else:
                    temp_res[col] = m[row][col] + min(res[col - 1], res[col], res[col + 1])

            res = temp_res  # Update the result list with the temporary result for the current row

        return min(res)  # Return the minimum sum from the last row

        
        # L=len(m)
        # res=m[0]
        # for i in range(L):
        #     print(res)
        #     c=i
        #     for row in range(1,L):
        #         if c>0 and c<(L-1):
        #             t=min(m[row][c],m[row][c+1],m[row][c-1])
        #             res[i]+=t
        #             if m[row][c+1]==t: c+=1
        #             elif m[row][c-1]==t: c-=1
        #         elif c==0:
        #             t=min(m[row][c],m[row][c+1])
        #             res[i]+=t
        #             if m[row][c+1]==t: c+=1
        #         elif c==(L-1):
        #             t=min(m[row][c],m[row][c-1])
        #             res[i]+=t
        #             if m[row][c-1]==t: c-=1
        #         # else:
        #         #     print("something went wrong")

        # return min(res)