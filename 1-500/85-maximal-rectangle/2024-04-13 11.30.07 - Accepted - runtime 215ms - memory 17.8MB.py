class Solution:
    ##### power by chatGPT #####
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        n = len(matrix[0])
        heights = [0] * (n + 1)
        max_area = 0
        
        for row in matrix:
            # Update the heights array based on the current row
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] == "1" else 0
            
            # Calculate the largest rectangle in the histogram formed by the heights
            stack = [-1]
            for j in range(n + 1):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[j]:
                    h = heights[stack.pop()]
                    w = j - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(j)
        
        return max_area