class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy=sum(c>0 for r in grid for c in r)
        xz=sum(max(r) for r in grid)
        yz=sum(max(r) for r in zip(*grid))

        return xy+xz+yz