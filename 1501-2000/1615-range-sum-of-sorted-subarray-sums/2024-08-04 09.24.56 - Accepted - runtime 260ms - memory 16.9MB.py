class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        heap=[(v,i) for i,v in enumerate(nums)]
        heapq.heapify(heap)
        
        res=0
        MOD=10**9+7
        
        for k in range(1,right+1):
            sum_val,i=heapq.heappop(heap)
            if k>=left:
                res=(res+sum_val)%MOD
            if i+1<n:
                heapq.heappush(heap, (sum_val+nums[i+1], i+1))
        
        
        return res