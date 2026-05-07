class Solution:
    def transpose(self, m: List[List[int]]) -> List[List[int]]:
        return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]