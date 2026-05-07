class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        curMod=0
        d={0:-1}
        
        for p,v in enumerate(nums):
            curMod+=v
            curMod%=k
            if curMod in d:
                if p-d[curMod]>1:
                    return True
            else:
                d[curMod]=p


        return False