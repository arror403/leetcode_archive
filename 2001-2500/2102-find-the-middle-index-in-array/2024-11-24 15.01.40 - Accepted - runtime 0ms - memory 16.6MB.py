class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        l,r=0,sum(nums[1:])
        L=len(nums)

        for i in range(L):
            if l==r:
                return i
            else:
                l+=nums[i]
                if i+1<L:
                    r-=nums[i+1]


        return -1