class Solution:
    def intersect(self, m: List[int], n: List[int]) -> List[int]:
        return  list((Counter(m)&Counter(n)).elements())