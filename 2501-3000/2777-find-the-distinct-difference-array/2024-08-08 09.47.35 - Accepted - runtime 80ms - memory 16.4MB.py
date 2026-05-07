class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        suffix=[0]*(n+1)
        seen_suffix=set()
        res=[]
        
        for i in range(n-1, -1, -1):
            seen_suffix.add(nums[i])
            suffix[i]=len(seen_suffix)

        seen_prefix=set()
        for i in range(n):
            seen_prefix.add(nums[i])
            res.append(len(seen_prefix)-suffix[i+1])


        return res