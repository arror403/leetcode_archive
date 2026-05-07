class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        def sort_diagonal(row, col):
            diagonal = []
            while row < rows and col < cols:
                diagonal.append(mat[row][col])
                row += 1
                col += 1
            diagonal.sort()

            # Update the matrix with the sorted diagonal
            while row > 0 and col > 0:
                row -= 1
                col -= 1
                mat[row][col] = diagonal.pop()

        # Sort diagonals starting from the topmost row
        for col in range(cols):
            sort_diagonal(0, col)

        # Sort diagonals starting from the leftmost column
        for row in range(1, rows):
            sort_diagonal(row, 0)

        return mat
