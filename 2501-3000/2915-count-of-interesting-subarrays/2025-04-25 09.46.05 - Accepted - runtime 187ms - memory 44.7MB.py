class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        res=total=0
        d=defaultdict(int)

        for i in range(len(nums)): nums[i]=1 if nums[i]%modulo==k else 0
            
        for i in range(len(nums)):
            total+=nums[i]
            mod_val=total%modulo

            if mod_val==k: res+=1

            find=mod_val-k
            if find<0: find+=modulo
            
            res+=d[find]
            d[mod_val]+=1
    
    
        return res