class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        L=len(nums)
        groupIndex=0

        nums.sort()
        res=[[0]*3 for _ in range(L//3)]
        
        for i in range(0, L, 3):
            if ((i+2)<L and nums[i+2]-nums[i]<=k):
                res[groupIndex] = nums[i], nums[i+1], nums[i+2]
                groupIndex+=1
            else:
                return []


        return res