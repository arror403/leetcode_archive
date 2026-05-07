class Solution:
    def findIntersectionValues(self, a: List[int], b: List[int]) -> List[int]:
        c=list(set(a)&set(b))
        return [sum(1 for i in a if i in c),sum(1 for i in b if i in c)]