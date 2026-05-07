class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left=0 
        right=10**7

        while left<right:
            mid=(left+right+1)//2
            S=sum(c//mid for c in candies)
            
            if k>S:
                right=mid-1
            else:
                left=mid
        

        return left