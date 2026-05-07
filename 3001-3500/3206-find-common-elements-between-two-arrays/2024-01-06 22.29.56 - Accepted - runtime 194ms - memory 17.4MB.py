class Solution:
    def findIntersectionValues(self, a: List[int], b: List[int]) -> List[int]:
        return [len([x for x in a if x in set(b)]),len([x for x in b if x in set(a)])]