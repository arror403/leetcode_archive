class Solution:
    def luckyNumbers (self, m: List[List[int]]) -> List[int]:
        return list(set(min(r) for r in m)&set(max(c) for c in zip(*m)))