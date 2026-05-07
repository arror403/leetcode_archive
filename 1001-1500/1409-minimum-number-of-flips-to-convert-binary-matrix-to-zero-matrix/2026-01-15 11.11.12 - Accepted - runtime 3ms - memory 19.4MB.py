class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])


        def flip(y, x):
            mat[y][x] ^= 1
            if(y - 1 >= 0): mat[y-1][x] ^= 1
            if(y + 1 <  n): mat[y+1][x] ^= 1
            if(x - 1 >= 0): mat[y][x-1] ^= 1
            if(x + 1 <  m): mat[y][x+1] ^= 1
            # print(mat)
            return mat
        

        def isZeroMat():
            for i in range(n):
                for j in range(m):
                    if mat[i][j]:
                        return False
            return True
        

        def FlipOrNotFlip(y, x):
            # Move to next row if we reached end of columns
            if x == m:
                y += 1
                x = 0
            
            # Base case: End of matrix
            if y == n: 
                return 0 if isZeroMat() else 10000

            # Option 1: Don't flip current cell
            # Because we use backtracking, the recursive call returns with 'mat' unchanged
            ret1 = FlipOrNotFlip(y, x+1)

            # Option 2: Flip current cell
            flip(y, x) # 1. Modify state
            ret2 = FlipOrNotFlip(y, x+1) + 1 # 2. Recurse
            flip(y, x) # 3. BACKTRACK (Restore state for the caller)

            return min(ret1, ret2)
        

        ret = FlipOrNotFlip(0, 0)

        return -1 if ret >= 10000 else ret