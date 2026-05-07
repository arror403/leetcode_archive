class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        t=list(map(lambda y:1 if (y in [(0,1),(1,0)]) else 0, pairwise(map(lambda x:x%2, nums))))
        prefix_sum=list(accumulate([0]+t))
        res=[]

        for a,b in queries:
            # Check if all elements in t[a:b] are True
            if prefix_sum[b]-prefix_sum[a]==(b-a):
                res+=[True]
            else:
                res+=[False]
        

        return res