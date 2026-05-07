class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        res=0
        mp=defaultdict(int)
        
        for i,v in enumerate(nums):
            res+=i-mp[i-v]
            mp[i-v]+=1


        return res