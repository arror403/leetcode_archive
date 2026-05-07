class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        t=list(map(lambda y:1 if (y in [(0,1),(1,0)]) else 0, pairwise(map(lambda x:x%2, nums))))
        p=list(accumulate([0]+t))

        return [p[b]-p[a]==(b-a) for a,b in queries]