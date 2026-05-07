class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        
        # 1. Build a 2D Prefix Sum Array (1-based index)
        # P[i][j] stores the sum of the rectangle from (0,0) to (i-1, j-1)
        P = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = (P[i-1][j] + P[i][j-1] - P[i-1][j-1] + mat[i-1][j-1])
        
        # 2. Iterate through the matrix and look for valid squares
        ans = 0
        
        # We iterate through every cell (i, j) treating it as the 
        # BOTTOM-RIGHT corner of a potential square.
        for i in range(m):
            for j in range(n):
                # We want to check if we can form a square larger than the one we already found.
                # If we found a square of size 3, we only care if we can find one of size 4.
                current_len = ans + 1
                
                # Check bounds: can a square of size 'current_len' end at (i, j)?
                if i - current_len + 1 >= 0 and j - current_len + 1 >= 0:
                    
                    # Calculate sum using Prefix Sum array in O(1)
                    # Coordinates in P map to:
                    # Bottom-Right: (i+1, j+1)
                    # Top-Left boundaries: (i+1 - current_len, j+1 - current_len)
                    
                    r1, c1 = i + 1 - current_len, j + 1 - current_len
                    r2, c2 = i + 1, j + 1
                    
                    total = P[r2][c2] - P[r1][c2] - P[r2][c1] + P[r1][c1]
                    
                    if total <= threshold:
                        ans += 1
                        
        return ans
        
        # m, n = len(mat), len(mat[0])
        # k = min(m, n)
        
        # for l in range(k, 0, -1):
        #     # tmp=[]
        #     for i in range(m - l + 1):
        #         for j in range(n - l + 1):
        #             # tmp.append([row[j:j+l] for row in mat[i:i+l]])
        #             if sum([sum(row[j:j+l]) for row in mat[i:i+l]]) <= threshold:
        #                 return l

        #     # print(tmp)
        #     # print('####')
        # return 0