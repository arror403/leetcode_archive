class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        d=[k for k,f in Counter(nums).items() if f==1]
        nums=dict.fromkeys(nums)
        res=[]

        for x in d:
            if (x+1) in nums or (x-1) in nums:
                continue
            else:
                res+=[x]

        return res