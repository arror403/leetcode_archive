class Solution:
    def diagonalSort(self, matrix: List[List[int]]) -> List[List[int]]:

        num_rows, num_cols = len(matrix), len(matrix[0])

        # Helper function to get the diagonal elements
        def get_diagonal_elements(start_row, start_col):
            diagonal = []
            while start_row < num_rows and start_col < num_cols:
                diagonal.append(matrix[start_row][start_col])
                start_row += 1
                start_col += 1
            return diagonal

        # Helper function to set the diagonal elements
        def set_diagonal_elements(start_row, start_col, sorted_diagonal):
            index = 0
            while start_row < num_rows and start_col < num_cols:
                matrix[start_row][start_col] = sorted_diagonal[index]
                start_row += 1
                start_col += 1
                index += 1

        # Iterate over the bottom-left diagonals
        for row in range(num_rows - 1, 0, -1):
            diagonal_elements = get_diagonal_elements(row, 0)
            diagonal_elements.sort()
            set_diagonal_elements(row, 0, diagonal_elements)

        # Iterate over the bottom-right diagonals
        for col in range(num_cols):
            diagonal_elements = get_diagonal_elements(0, col)
            diagonal_elements.sort()
            set_diagonal_elements(0, col, diagonal_elements)

        return matrix



        # print([sorted(i) for i in self.convert_util(mat)])
        # print(self.from_diagonals(mat))
        # return self.from_diagonals([sorted(i) for i in self.convert_util(mat)])
        # print([sorted(i) for i in self.convert_util(mat)])
        # return [[]]



    # def convert_util(self, matrix):
    #     if not matrix: return []

    #     num_rows, num_cols = len(matrix), len(matrix[0])
    #     result = []

    #     # Traverse diagonals starting from the top-left corner
    #     for d in range(num_rows + num_cols - 1):
    #         row = max(0, num_rows - 1 - d)
    #         col = max(0, d - num_rows + 1)
    #         diagonal = []

    #         while row < num_rows and col < num_cols:
    #             diagonal.append(matrix[row][col])
    #             row += 1
    #             col += 1

    #         result.append(diagonal)

    #     return result

    # def from_diagonals(self, diagonal_lists):
    #     if not diagonal_lists:
    #         return []

    #     max_len = max(len(diagonal) for diagonal in diagonal_lists)
    #     result = []

    #     for i in range(max_len):
    #         row = []
    #         for diagonal in diagonal_lists:
    #             if i < len(diagonal):
    #                 row.append(diagonal[-(i + 1)])
    #         result.insert(0, row)

    #     return result