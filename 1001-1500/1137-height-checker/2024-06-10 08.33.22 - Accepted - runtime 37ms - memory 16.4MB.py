class Solution:
    def heightChecker(self, m: List[int]) -> int:
        return sum(1 for a,b in zip(m,sorted(m)) if a!=b)