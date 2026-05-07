class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        c=len(matrix)
        return all(len(set(i))==c for i in matrix) and all(len(set(i))==c for i in zip(*matrix))
        