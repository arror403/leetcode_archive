class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return len([c for r in grid for c in r if c]) + sum(max(r) for r in grid) + sum(max(c) for c in zip(*grid))