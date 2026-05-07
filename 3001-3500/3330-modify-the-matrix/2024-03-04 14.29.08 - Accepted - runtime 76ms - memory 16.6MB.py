class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        return zip(*[[max(i) if j==-1 else j for j in i] for i in zip(*matrix)])