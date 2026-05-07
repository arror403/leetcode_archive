class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(v<k for v in nums): return -1

        nums=sorted(set(nums), reverse=True)
        
        if len(nums)==1 and nums[0]==k: return 0
        
        res=i=0
        L=len(nums)

        while i<L and nums[i]>k:
            current=nums[i]
            i+=1
            res+=1
        

        return res
        


# class Solution:
#     def minOperations(self, nums: List[int], k: int) -> int:
#         if len(set(nums))==1:
#             if nums[0]==k:
#                 return 0

#         t=sum(v>k for v in set(nums))


#         return t if t else -1