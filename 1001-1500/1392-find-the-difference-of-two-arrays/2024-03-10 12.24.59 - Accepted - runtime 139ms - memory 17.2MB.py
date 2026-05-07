class Solution:
    def findDifference(self, m: List[int], n: List[int]) -> List[List[int]]:
        return [list(set(m)-set(n)),list(set(n)-set(m))]