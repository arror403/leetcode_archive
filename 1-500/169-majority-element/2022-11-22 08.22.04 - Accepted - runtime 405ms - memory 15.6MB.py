class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in dict.fromkeys(nums): d[i]=0
        for i in nums: d[i]+=1
        print((len(nums)//2),d)
        for k,v in d.items():
            if v>(len(nums)//2):
                return k
