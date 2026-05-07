class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res=1
        if 0 in nums: return 0
        else:
            for i in nums:
                res*=i
                
            if res>0: return 1
            elif res<0: return -1
            else: return 0