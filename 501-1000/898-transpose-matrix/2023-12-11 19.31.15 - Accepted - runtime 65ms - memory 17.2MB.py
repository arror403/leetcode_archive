class Solution:
    def transpose(self, m: List[List[int]]) -> List[List[int]]:
        return zip(*m)