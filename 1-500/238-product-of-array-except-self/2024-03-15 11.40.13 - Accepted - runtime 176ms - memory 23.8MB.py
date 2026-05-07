class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if all([i==0 for i in nums]): return nums

        p=reduce(lambda x,y:x*y, [i for i in nums if i!=0])

        # If there are more than one zero, result should be all zeros except at those positions
        if nums.count(0)>1: return [0]*len(nums)
        # If there is exactly one zero, result should be product at zeros and zeros elsewhere
        elif nums.count(0)==1: return [p if x==0 else 0 for x in nums]
        # If there are no zeros, result should be product divided by each element
        else: return [p//x for x in nums]