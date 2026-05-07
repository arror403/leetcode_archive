class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return target in list(chain.from_iterable(matrix))
