class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        left = [0] * n
        right = [n] * n
        height = [0] * n
        max_area = 0
        
        for i in range(m):
            curr_left, curr_right = 0, n
            
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                    left[j] = max(left[j], curr_left)
                else:
                    height[j] = 0
                    left[j] = 0
                    curr_left = j + 1
            
            for j in range(n-1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], curr_right)
                else:
                    right[j] = n
                    curr_right = j
                max_area = max(max_area, height[j] * (right[j] - left[j]))
        

        return max_area