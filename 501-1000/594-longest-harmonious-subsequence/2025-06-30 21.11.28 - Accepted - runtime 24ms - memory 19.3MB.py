class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d=Counter(nums)
        res=0

        for x in d:
            if x+1 in d:
                res=max(res, d[x]+d[x+1])
        
        
        return res


        # res=-1
        # m=[[i,v] for i,v in enumerate(nums)]
        # m.sort(key=lambda x:x[1])

        # for a,b in pairwise(m):
        #     if (b[1]-a[1])==1:
        #         res=max(res, abs(a[0]-b[0]))


        # return res+1