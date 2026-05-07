class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        t=[0]+[int(y in [(0,1),(1,0)]) for y in pairwise(x%2 for x in nums)]
        p=list(accumulate(t))

        return [p[b]-p[a]==(b-a) for a,b in queries]