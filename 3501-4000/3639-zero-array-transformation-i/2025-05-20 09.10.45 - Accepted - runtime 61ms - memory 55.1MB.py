class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n=len(nums)
        freq=[0]*(n+1)

        for l,r in queries:
            freq[l]+=1
            freq[r+1]-=1
        
        op=0
        for i in range(n):
            op+=freq[i]
            if op<nums[i]: return False

        return True