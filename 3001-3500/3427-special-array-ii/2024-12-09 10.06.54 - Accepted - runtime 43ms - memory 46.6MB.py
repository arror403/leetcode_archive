class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        t=[False]+[(y[0]+y[1])==1 for y in pairwise(x%2 for x in nums)]
        p=list(accumulate(t))

        return [p[b]-p[a]==(b-a) for a,b in queries]