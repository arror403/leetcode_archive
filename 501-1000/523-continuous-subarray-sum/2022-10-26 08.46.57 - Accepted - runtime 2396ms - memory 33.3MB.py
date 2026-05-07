class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        curMod=0
        dic={0:-1} #key:mod,val:pos
        for pos,val in enumerate(nums):
            #每次累加，取餘數
            curMod+=val
            curMod%=k
            if curMod in dic:
                #需大於1，ex: nums=[0],k=1這種極端case應為False
                if pos-dic[curMod]>1:
                    return True
            else:
                dic[curMod]=pos
        return False