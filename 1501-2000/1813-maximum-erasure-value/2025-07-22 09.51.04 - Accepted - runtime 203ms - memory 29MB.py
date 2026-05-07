class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res=cur=l=0
        s=set()

        for r in range(len(nums)):
            while nums[r] in s:
            # while (!set.add(nums[r])):
                cur-=nums[l]
                s.remove(nums[l])
                l+=1

            # Add the current element to set and update score
            s.add(nums[r])
            
            cur+=nums[r]
            res=max(res, cur)
            

        return res