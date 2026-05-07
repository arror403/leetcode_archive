class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        return target[0] + sum(b-a if b>a else 0 for a,b in pairwise(target))