class Solution:
    def sortColors(self, nums: List[int]) -> None:
        d=Counter(nums)
        x=0
        for _ in range(d[0]):
            nums[x]=0
            x+=1
        for _ in range(d[1]):
            nums[x]=1
            x+=1
        for _ in range(d[2]):
            nums[x]=2
            x+=1