class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Create an n x n matrix filled with zeros
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        # Define the four borders of the matrix
        top, bottom, left, right = 0, n - 1, 0, n - 1
        
        # Initialize the current number to 1
        current_num = 1
        
        # Loop until the current number equals n^2
        while current_num <= n * n:
            # Traverse the top row from left to right
            for i in range(left, right + 1):
                matrix[top][i] = current_num
                current_num += 1
            top += 1
            
            # Traverse the right column from top to bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = current_num
                current_num += 1
            right -= 1
            
            # Traverse the bottom row from right to left
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = current_num
                current_num += 1
            bottom -= 1
            
            # Traverse the left column from bottom to top
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = current_num
                current_num += 1
            left += 1
        
        return matrix