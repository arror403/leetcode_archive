class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        L=len(nums)
        res=L
        a,b=[0]*L,[0]*L
        v=[]
        
        # Forward pass
        for i in range(L):
            x = nums[i]
            it = bisect.bisect_left(v, x)
            a[i] = it  # Not len(v), but the position where x would be inserted
            if it != len(v):
                v[it] = x
            else:
                v.append(x)
                
        v = []
        # Backward pass
        for i in range(L-1,-1,-1):
            x = nums[i]
            it = bisect.bisect_left(v, x)
            b[i] = it  # Not len(v), but the position where x would be inserted
            if it != len(v):
                v[it] = x
            else:
                v.append(x)
                
        # Calculate minimum length
        for i in range(1,L):
            if a[i] and b[i]:  # If both sides have smaller elements
                res = min(res, L-(a[i]+b[i]+1))
                

        return res



        # for i in range(L):
        #     x=nums[i]
        #     it=bisect.bisect_left(v,x,0,len(v))
        #     a[i]=it-v[0]
        #     if it!=v[-1]: it=x
        #     else: v.append(x)

        # v=[]

        # for i in range(L-1,-1,-1):
        #     x=nums[i]
        #     it=bisect.bisect_left(v,x,0,len(v))
        #     b[i]=it-v[0]
        #     if it!=v[-1]: it=x
        #     else: v.append(x)

        # for i in range(1,L):
        #     if a[i] and b[i]: res=min(res, L-(a[i]+b[i]+1))


        # return res