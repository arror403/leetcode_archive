class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)
        res=1
        MOD=10**9+7

        # Increment the smallest element k times
        for _ in range(k):
            smallest=heappop(nums)
            heappush(nums, smallest+1)
        
        # Calculate the product
        for v in nums: res=(res*v)%MOD
            
        
        return res