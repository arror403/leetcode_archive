class Solution:
    def findIntersectionValues(self, a: List[int], b: List[int]) -> List[int]:
        set_a=set(a)
        set_b=set(b)
        return [len([x for x in a if x in set_b]),len([x for x in b if x in set_a])]