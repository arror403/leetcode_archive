class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        d=defaultdict(int)
        for xi,yi in zip(x,y): d[xi]=max(d[xi], yi)

        if len(d)<3: return -1


        return sum(nlargest(3, d.values()))