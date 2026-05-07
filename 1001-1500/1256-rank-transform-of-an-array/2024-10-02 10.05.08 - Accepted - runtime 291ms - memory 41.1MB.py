class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d=sorted(Counter(arr).items())
        r={v[0]:i+1 for i,v in enumerate(d)}

        return [r[v] for v in arr]