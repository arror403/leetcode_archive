class Solution:
    ##### power by Claude #####
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            count={}
            res,i=0,0
            for j in range(len(nums)):
                count[nums[j]]=count.get(nums[j],0)+1
                while len(count)>k:
                    count[nums[i]]-=1
                    if count[nums[i]]==0:
                        del count[nums[i]]
                    i+=1
                res+=(j-i+1)
            return res

        return atMost(k)-atMost(k-1)