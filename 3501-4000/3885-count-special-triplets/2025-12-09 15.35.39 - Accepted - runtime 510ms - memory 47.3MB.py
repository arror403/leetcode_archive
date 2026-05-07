class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        d=defaultdict(list)
        res=0

        for i,v in enumerate(nums): d[v].append(i)

        for i in range(1, len(nums)-1):
            v=nums[i]*2
            
            if v in d:
                p=bisect_left(d[v], i)
                q=len(d[v])-bisect_right(d[v], i)
                res += p*q


        return res%(10**9+7)