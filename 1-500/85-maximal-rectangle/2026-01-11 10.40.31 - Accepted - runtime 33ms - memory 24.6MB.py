class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0]) 
        left = [0]*n
        right = [n]*n
        height = [0]*n
        maxA = 0

        for i in range(m):
            cur_left = 0
            cur_right = n
            # compute height (can do this from either side)
            for j in range(n):
                if matrix[i][j]=='1':
                    height[j]+=1
                else:
                    height[j]=0
            # compute left (from left to right)
            for j in range(n):
                if matrix[i][j]=='1': 
                    left[j] = max(left[j], cur_left)
                else: 
                    left[j] = 0 
                    cur_left = j+1
            # compute right (from right to left)
            for j in range(n-1, -1, -1):
                if matrix[i][j]=='1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # compute the area of rectangle (can do this from either side)
            for j in range(n):
                maxA = max(maxA, (right[j]-left[j])*height[j])
        

        return maxA