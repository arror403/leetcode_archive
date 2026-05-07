class Solution:
    def findIntersectionValues(self, a: List[int], b: List[int]) -> List[int]:
        return [sum(1 for i in a if i in set(b)),sum(1 for i in b if i in set(a))]