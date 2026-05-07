class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        L=len(nums)
        if L%2==0:
            t=[nums[i]+nums[i+1] for i in range(0,L,2)]
        else:
            t=[nums[i]+nums[i+1] for i in range(0,L-1,2)]

        return [len(list(g)) for _,g in groupby(t)][0]