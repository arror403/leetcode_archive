class Solution:
    def countPoints(self, rings: str) -> int:
        d=defaultdict(set)
        for r,c in zip(rings[1::2],rings[::2]): d[r].add(c)

        return sum(1 for x in d.values() if x=={'R','B','G'})