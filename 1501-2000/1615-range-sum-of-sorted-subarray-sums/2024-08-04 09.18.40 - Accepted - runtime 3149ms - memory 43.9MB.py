class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l=0
        m=[]
        
        while l<n:
            for i in range(n-l):
                m.append(sum(nums[i:i+l+1]))
            l+=1
        
        return sum(sorted(m)[left-1:right])%(10**9+7)