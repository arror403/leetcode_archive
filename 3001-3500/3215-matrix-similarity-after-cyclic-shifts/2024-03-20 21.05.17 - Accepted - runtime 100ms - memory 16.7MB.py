class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        
        # Function to cyclically shift a row to the right by k positions
        def cyclic_right_shift(row, k):
            k %= len(row)
            return row[-k:] + row[:-k]
        
        # Function to cyclically shift a row to the left by k positions
        def cyclic_left_shift(row, k):
            k %= len(row)
            return row[k:] + row[:k]
        
        # Create a new matrix to store the modified rows
        new_mat = []
        
        # Perform cyclic shifts on rows based on their index
        for i, row in enumerate(mat):
            if i % 2 == 0:
                new_mat.append(cyclic_left_shift(row, k))
            else:
                new_mat.append(cyclic_right_shift(row, k))
        
        # Check if the initial and final matrices are the same
        for i in range(m):
            for j in range(n):
                if new_mat[i][j] != mat[i][j]:
                    return False
        return True
