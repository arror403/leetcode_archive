class Solution:
    def findIntersectionValues(self, a: List[int], b: List[int]) -> List[int]:
        return [sum(f for v,f in Counter(a).items() if v in Counter(b).keys()),
                sum(f for v,f in Counter(b).items() if v in Counter(a).keys())]